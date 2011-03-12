$(document).ready(function() {
    $('a').click(function(){ window.location=$(this).attr('href'); });
    $('#editable').blur(function() {
        var newValue = $(this).html();
        var that = this;
        // do something         
        // For example, you could place an AJAX call here:  
        alert("Sending: " +newValue);
        $.ajax({
           type: "POST",
           url: window.location.pathname,
           data: "text=" + newValue + "&action=write",
           success: function(data) {
               data = jQuery.parseJSON(data);
               alert(data.Message);
               $(that).html(data.Message);
               $('a').click(function(){ window.location=$(this).attr('href'); });
           }
        });
    });
});
