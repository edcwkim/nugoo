$(function() {
  $.ajax({
      url="https://nugoo.me/people/names";
      success: function(data) {
          var names = data.data,
              selector = "";
          var flag = 0;
          console.log(names);
          
          // highlight all the names in names
          for (var i = 0; i < names.length; ++i) {
            var selector = "body :contains('" + names[i] + "')";

            $(selector).each(function(_, element) {
              $(element).html(function(_, oldHtml) {
                var regexp = new RegExp("(>[^<]*)" + names[i], "gmu"),
                    span = '<span class="nugoo nugoo-' + i + '">' + names[i] + '</span>';
                return oldHtml.replace(regexp, "$1" + span);
              });
            });
          }
          
          for (var i=0; i< names.length; ++i) {
            $(".nugoo-" + i).tooltip({
              items: ".nugoo-" + i,
              content: '<iframe src="https://nugoo.me/p/' + names[i] + '/" width="400" height="224" style="border: none;"></iframe>',
              classes: {"ui-tooltip": "nugoo-tooltip"}
            });
          }

          var headers = $(".nugoo");
          
          $(headers).each(function(index) {
            $(this).on("mouseenter", function (e) {
                console.log("Before : " + flag);
                if (flag == 0) {
                    e.stopImmediatePropagation();
                    $(this).tooltip("enable");
                    $(this).tooltip("open");
                    flag = 1
                    console.log("After : " + flag);
                } else {
                    $(this).tooltip("disable");
                }
            });

            $(this).on("mouseleave", function (e) {
                e.stopImmediatePropagation();
            });

          });

          $(document).mouseup(function (e) {
              var container = $(".ui-tooltip");
              if (! container.is(e.target) && 
                  container.has(e.target).length === 0)
              {
                  $(".nugoo").tooltip("disable");
                  flag = 0;
                  console.log("Now : " + flag);
              }
          });
      }
  });
});
