$(document).ready(function () {
  "use strict";

  $(".section--bg, .details__bg").each(function () {
    if ($(this).attr("data-bg")) {
      $(this).css({
        background: "url(" + $(this).data("bg") + ")",
        "background-position": "center center",
        "background-repeat": "no-repeat",
        "background-size": "cover",
      });
    }
  });

  $(".accordion").mCustomScrollbar({
    axis: "y",
    scrollbarPosition: "outside",
    theme: "custom-bar",
  });

  // $('.card__description--details').moreLines({
  //     linecount: 6,
  //     baseclass: 'b-description',
  //     basejsclass: 'js-description',
  //     classspecific: '_readmore',
  //     buttontxtmore: "",
  //     buttontxtless: "",
  //     animationspeed: 400
  // });
});
