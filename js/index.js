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
            C02: $("#C02").val(),
            light:$("#light").val(),
            humidity_ratio:$("#humidity_ratio").val()
    }
        ),
        success: (data)=>{
            console.log(data)
        },
        statusCode: {
            201: (data) => {
                console.log("post request successful")
            },
        },
        error:(err)=> {
            console.log(err)
            console.log("error doing post request")
        }
    })
});