var url_string = window.location.href
var url = new URL(url_string);
var fraud = url.searchParams.get("fraud");

if(fraud == "N"){
    document.getElementById("output_display").innerHTML = "<h3>No Fraud Detected</h3>"
    var NP = url.searchParams.get("NP");
    document.getElementById("output_percentage").innerHTML = "<h4>The system is "+ NP +"% sure for no fraud.</h4>"
}
else{
    document.getElementById("output_display").innerHTML = "<h3>Fraud Detected</h3>"
    var NP = url.searchParams.get("PP");
    document.getElementById("output_percentage").innerHTML = "<h4>The system is "+ PP +"% sure for fraud.</h4>"
}