$("#predict").click((e) => {
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/predict',
        contentType:'application/json',
        dataType:'json',
        data: JSON.stringify(
            {temperature: $("#temperature").val(),
            humidity: $("#humidity").val(),
            light:$("#light").val(),
            C02: $("#C02").val(),
            humidity_ratio:$("#humidity_ratio").val()
    }
        ),

        statusCode: {
            201: (data) => {
                console.log("post request successful");
                location = '/displayPrediction/' + data;
            },
        },
        error:(err)=> {
            console.log(err);
            console.log("error doing post request");
        }
    })
});