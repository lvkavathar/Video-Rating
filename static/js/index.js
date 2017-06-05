$(document).ready(function(){
	initialFunction();
});

function initialFunction() {
    let DataFetchCommand;
    $("#buttonSearchID").click(function(){
        $(".dimScreen").show();
        $("#headerID").hide();
        let webURL = document.getElementById("textSearchInput").value;
        let newWebURL = webURL.split("?v=")[1];
        DataFetchCommand = newWebURL.split("&")[0];
        sendHackVideoURL(DataFetchCommand);
    });
}

function sendHackVideoURL(DataFetchCommand) {
  $.ajax({
      type: 'get',
      dataType: 'text',
      url: 'http://ec2-52-89-34-25.us-west-2.compute.amazonaws.com:5000/api/url',
      async: false,
      data: {
        "cmd" : DataFetchCommand
      },
      success: function (result, status) {
        console.log(result);
          //getRawDataJSON(result);
          $(".dimScreen").hide();
          $("#headerID").show();
      },
      error: function(res) {
          alert("Server Error:" + res.responseText + ".\nError occurred while retrieving values for the search Tab.");
          $(".dimScreen").hide();
          $("#headerID").show();
      }
    }
  );
}
