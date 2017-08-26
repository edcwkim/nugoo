$(function() {
  $.ajax({
    url: "https://b31a79b7.ngrok.io/people/names/",
    success: function(data) {
      var names = data.data,
          selector = "";

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
