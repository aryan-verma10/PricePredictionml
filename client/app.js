
function onPageLoad(){
    console.log("document loaded")
    var url = "http://127.0.0.1:5000/get_location_name";
    $.get(url, function(data, status){
        console.log("got response for get_location_name request");
        if(data){
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $("#uiLocations").empty();
//            console.log(uiLocations);
            for(var i in locations){
                var opt = new Option(locations[i]);
//                console.log(opt);
                $(uiLocations).append(opt);
            }
        }
    });
}

// this is returning number of bhks checked
function getBHKvalue() {
    var uibhk = document.getElementsByName("uiBHK");
    for( var i in uibhk)
    {
        if(uibhk[i].checked)  // used to check the check box
        {
            return parseInt(i) + 1;     // this function return integer as i is string
        }
    }
    return -1;
}


// this function is used to request for the estimate price from server
function onClickedEstimatePrice(){
        console.log("Estimate Price button clicked");
        var area = document.getElementById("uisqft");
        var bhk = getBHKvalue();
        var location = document.getElementById("uiLocations");
        var estPrice = document.getElementById("uiEstimatedPrice");

        var url = "http://127.0.0.1:5000/predict_home_price";

        // now we will make a post call to the server
        $.post(url, {
        area : parseFloat(area.value),
        bhk : bhk,
        location: location.value
        }, function(data, status){
            estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "</h2>";
            console.log(status);
        }
       )
}

window.onload = onPageLoad; // when a page is loaded first thing this happens