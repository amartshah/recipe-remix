var RECIPE = {};
var STEPS = [];

function displayRecipe(recipe, steps) {
  var recipeToDisplay
  var title = recipe.name;
  var titleHTML ='<h2>'+title+'</h2>';
  recipeToDisplay = titleHTML;
  var ingHTML = '<h3><u>Ingredients:</u></h3>';
  var ingredients = recipe.ingredients;
  ingredients.forEach(function(ing) {
    if(ing.name){
      var thisHTML = '<p><b>' + ing.descriptor+' '+ing.name + ':</b> '+((ing.quantity != 0) ? ing.quantity : '')+' '+((ing.measurement != 'discrete') ? ing.measurement : '')+' '+ ((ing['prep-descriptor'] != null) ? ing['prep-descriptor'] : '')+ ' '+ing.preparation+'</p>';
      ingHTML += thisHTML;
    }

  });
  recipeToDisplay += ingHTML;

  var stepsHTML = '<h3><u>Steps:</u></h3>';
  var i = 1;
  steps.forEach(function(s){
      stepsHTML+= '<p>'+i+': '+s+'</p>';
      i++;
  });
  recipeToDisplay += stepsHTML;

  var tools = recipe['cooking tools'];
  var toolHTML = '</br><p><b>Tools:</b> ';

  tools.forEach(function(t){
    toolHTML+= t+', ';
  });
  toolHTML = toolHTML.substring(0, toolHTML.length - 2);

  recipeToDisplay += toolHTML+'</p>';

  var methods = recipe['cooking methods'];
  var methodHTML = '<p><b>Cooking Methods:</b> ';

  methods.forEach(function(m){
    if (m == recipe['primary cooking method']){
      methodHTML+= m+' (Primary), ';;
    }
    else{
      methodHTML+= m+', ';
    }

  });
  methodHTML = methodHTML.substring(0, methodHTML.length - 2);
  recipeToDisplay += methodHTML + '</p></br>';

  return recipeToDisplay;
}

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

      var recipeToDisplay = displayRecipe(resp['recipe'], resp['steps']);

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

      var recipeToDisplay = displayRecipe(resp['recipe'], resp['steps'])

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
