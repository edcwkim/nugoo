$(function() {
  $.ajax({
    url: "https://nugoo.me/people/names/",
    success: function(data) {
      var names = data.data,
          selector = "";

      // highlight all the names in names
      for (var i = 0; i < names.length; ++i) {
        selector = ":not(iframe) body :contains('"+ names[i] + "')";

        $(selector).each(function(_, element) {
          $(element).html(function(_, oldHtml) {
            var regexp = new RegExp("(>[^<]*)" + names[i], "gmu");
            return oldHtml.replace(regexp, "$1<span class='nugoo nugoo-" + i + "'>" + names[i] + "</span>");
          });
        });

        $(".nugoo-" + i).tooltip({
          items : ".nugoo-" + i,
          content : '<iframe src="https://nugoo.me/p/' + names[i] + '/"></iframe>'
        });
      }
    }
  });
});
