/*
$(function() {

  var names = ["이재용", "이건희", "이혁"],
    selector = "";

  console.log("names "+names);

  // highlight all the names in names
  for (var i = 0; i < names.length; ++i) {
    selector = ":contains('"+ names[i] + "')";
    console.log(selector);

    $("body" + selector).html(function(_, html) {
      return html.split(names[i]).join("<span class='nugoo' id='nugoo" + names[i] + "' >" + names[i] + "</span>");
    });
  }

  // tooltip function
  for (var i = 0; i < names.length; ++i) {
    selector = ":contains('"+ names[i] + "')";
    console.log(selector);

    $("#nugoo"+names[i]).tooltip({
      items : "#nugoo" + names[i],
      //content : "<iframe src='https://www.w3schools.com'></iframe>"
      content : "<b>" + names[i] + "내용</b>"
    });
  }

});
*/
/*
$(function() {

  var names = ["이재용", "이건희", "이혁"],
    selector = "";

  console.log("names "+names);

  // highlight all the names in names
  for (var i = 0; i < names.length; ++i) {
    selector = ":contains('"+ names[i] + "')";
    console.log(selector);

    $("body" + selector).html(function(_, html) {
      return html.split(names[i]).join("<span class='nugoo"+ names[i] + "' >" + names[i] + "</span>");
    });
  }

  // tooltip function
  for (var i = 0; i < names.length; ++i) {
    selector = ":contains('"+ names[i] + "')";
    console.log(selector);

    $(".nugoo"+names[i]).tooltip({
      items : ".nugoo" + names[i],
      //content : "<iframe src='https://www.w3schools.com'></iframe>"
      content : "<b>" + names[i] + "내용</b>"
    });
  }

});
*/

$(function() {
  $.ajax({
    url: "https://nugoo.me/people/names/",
    success: function(data) {
      var names = data.data,
      selector = "";

      // highlight all the names in names
      for (var i = 0; i < names.length; ++i) {
        selector = "body :contains('"+ names[i] + "')";

        $(selector).each(function(_, element) {
          $(element).html(function(_, oldHtml) {
            // return oldHtml.replace(/regex???/g)
            return oldHtml.split(names[i]).join("<span class='nugoo nugoo-" + i + "'>" + names[i] + "</span>");
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
