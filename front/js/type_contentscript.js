/*
$(function() {
  $.ajax({
    url: "https://b31a79b7.ngrok.io/people/names/",
    success: function(data) {
      var names = data.data,
          selector = "";
	  
	  console.log("names "+names);
      for (var i = 0; i < names.length; ++i)
        selector += ":contains('"+ names[i] + "'), ";
	
      if (selector.length)
        selector = selector.slice(0, -2);
      console.log(selector);

      $("body").contents()
               .filter(selector)
               .wrap("<b></b>");
    }
  });
});
*/
$(function() {

	$("body:contains('이재용')").html(function(_, html) {
		return html.split('이재용').join("<span class='nugu'>이재용</span>");
	});
	//var replace_str = $('body').html().replace(/contracting/g, '<strong>contracting</strong>'); 
	//$('body').html(replace_str);
});
