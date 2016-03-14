$( document ).ready(function() {
  $('#transform-actions').hide();

  $("#url-submit").click( function() {
    $('#original-recipe-display').html('<img src="http://designhousegarments.com/images/loading.gif"></img>');
    $.ajax({
      type: "POST",
      url: '/api/parse',
      data: { 'recipeUrl': $('#url-field').val() },
      success: function(resp) {
	console.log(resp);

	$('#original-recipe-display').html(resp)


	$('#transform-actions').show();
	$('#transform-submit').click( function() {
	  $('#transformed-display').html('<img src="http://designhousegarments.com/images/loading.gif"></img>');
	});
      }
    });
  });
});
