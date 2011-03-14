$(document).ready(function() {
    $('a').click(function(){ window.location=$(this).attr('href'); });
    $('#editable').blur(function() {
        var newValue = $(this).html();
        //alert("Sending: " +newValue);
        $.ajax({
           type: "POST",
           url: window.location.pathname,
           data: "text=" + newValue + "&action=write",
           success: editCallback
        });
    });
    $('#name').blur(function() {
        var newValue = $(this).html();
        //alert("Sending: " +newValue);
        $.ajax({
           type: "POST",
           url: window.location.pathname,
           data: "name=" + newValue + "&action=rename",
           success: renameCallback
        });
    });
    $('#message').click(function(){
       $(this).slideUp('200');
    });
});


function renameCallback(data) {
    data = jQuery.parseJSON(data);
    //alert(data.Message);
    if (data.Code == 1) {
        showMessage("Successfully renamed " + data.oldURL + " to " + data.newURL, data.Code);
        history.pushState(null, null, data.newURL);
    }
    else {
        showMessage(data.Message, data.Code);
    }
}

function editCallback(data) {
    data = jQuery.parseJSON(data);
    //alert(data.Message);
    if (data.Code == 1) {
        $('#editable').html(data.Message);
        $('a').click(function(){ window.location=$(this).attr('href'); });        
    }
    else {
        showMessage(data.Message, data.Code);
    }
}

function showMessage(message, code) {
    var bg = "#EFE";
    var color = "#696";
    if(code == 0) {
        bg = "#FEE";
        color = "#966";
    }
    $('#message').text(message);
    $('#message').css('color',color).css('background-color',bg);
    $('#message').slideDown('400');
    if(code != 1){
        setTimeout(function(){$('#message').slideUp('400');}, 4000);
    }
}


