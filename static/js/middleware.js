var RECIPE = {};
var STEPS = [];

function resetAll() {
  $('#transformed-display').html('');
  $('#transform-actions').html('');
  $('#original-recipe-display').html('');
  $('#url-field').val('');
  RECIPE = {};
  STEPS = [];
}

function transformRecipe() {
  $('#transformed-display').html('<img src="http://designhousegarments.com/images/loading.gif"></img>');
  $('#transform-submit').hide();

  var requestData = {
    'recipe': JSON.stringify(RECIPE),
    'steps': JSON.stringify(STEPS),
    'transformation': $('#transform-select').val()
  };

  $.ajax({
    type: "POST",
    url: '/api/transform',
    data: requestData,
    error: function(e) { console.log(e) },
    success: function(resp) {
      console.log(resp);

      var recipeToDisplay = '<pre>' + JSON.stringify(resp, null, 2) + '</pre>';

      $('#transformed-display').html(recipeToDisplay);
      var resetButton = '<button id="reset-button">Reset</button>';
      $('#transformed-display').append(resetButton);
      $('#reset-button').click(resetAll);
      $('#transform-submit').show();
    }
  });
}

function submitUrl() {
  $('#original-recipe-display').html('<img src="http://designhousegarments.com/images/loading.gif"></img>');
  $('#url-submit').hide();

  $.ajax({
    type: "POST",
    url: '/api/parse',
    data: { 'recipeUrl': $('#url-field').val() },
    success: function(resp) {
      console.log(resp);
      RECIPE = resp['recipe'];
      STEPS = resp['steps'];

      var recipeToDisplay = '<pre>' + JSON.stringify(resp['recipe'], null, 2) + '</pre>';
      recipeToDisplay += '<pre>' + JSON.stringify(resp['steps'], null, 2) + '</pre>';

      $('#original-recipe-display').html(recipeToDisplay);
      $('#transform-actions').show();
      $('#transform-submit').click(transformRecipe);
      $('#url-submit').show();
    }
  });
}


$( document ).ready(function() {
  $('#transform-actions').hide();
  $("#url-submit").click(submitUrl);
});
