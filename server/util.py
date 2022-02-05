import json
import pickle
import numpy as np
# get location function read the column.json file and provide all location names
__location = None
__data_columns = None
__model1 = None
__model2 = None

def get_estimated_price(location, area, bhk):
    try:
        loc_index = __data_columns.index(location.lower())

    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = bhk


    x[loc_index] = 1
    return round(__model1.predict([x])[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __location
    global __model1
    global __model2

    with open("artifact/columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]   # this returns the list
        __location = __data_columns[2:]     # as locations start from 2 index

    with open("artifact/Delhi_home_price_model_linear.pickle", 'rb') as f:
        __model1 = pickle.load(f)

    with open("artifact/Delhi_home_price_model_quad.pickle", "rb") as f2:
        __model2 = pickle.load(f2)

    print("loaading artifacts is done....")

def get_location():
    return __location

def get_data_columns():
    return __data_columns

# if __name__ == '__main__':
load_saved_artifacts()

