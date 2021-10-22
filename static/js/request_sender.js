console.log("Hello")

$('#submit_details').click(function(){
    var serializedData = $("#fraud_detection").serialize();
    console.log($("#hobby").value, "HE", serializedData)

    $.ajax({
        headers: { "X-CSRFToken": csrftoken },
        url: '/fraud_detection',
        data: serializedData,
        type: 'POST',

        success: function(response){
            console.log(response)
            var arr = response.split(",")
            window.location = "http://127.0.0.1:8000/result?fraud="+arr[0]+"&NP="+arr[1]+"&PP="+arr[2];
        }
    });

});