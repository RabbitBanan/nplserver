
function send_messages() {

  var form_data = {
    'name': $('#name').val(),
    'text': $('#text').val()
  }
  $('#messege-box').append("<p>"+ form_data.text +"</>");
  console.log(form_data);
  //$('#messege-box').append("<samp>"+ form_data.text +"</samp>");
  $.ajax({
      type: "POST",
      url: "/send_messages",
      data: form_data,
      success: function (data) {
        $('#messege-box').append("<p>"+ data.answer +"</>");
        $('#text').val('')
      }
  })
}
