$(document).ready(function () {
  "use strict";

  $(".scrollbar-dropdown").mCustomScrollbar({
    axis: "y",
    scrollbarPosition: "outside",
    theme: "custom-bar",
  });

  $(".section--bg").each(function () {
    if ($(this).attr("data-bg")) {
      $(this).css({
        background: "url(" + $(this).data("bg") + ")",
        "background-position": "center center",
        "background-repeat": "no-repeat",
        "background-size": "cover",
      });
    }
  });

  $(".filter__item-menu li").on("click", function () {
    let text = $(this).text();
    let dataValue = $(this).attr("data-value");
    let item = $(this);
    let id = $("#" + item.closest(".filter__item").attr("id"));
    if (text.includes("Any")) {
      id.find('.filter__item-btn input[type="button"]').val(text);
      id.find('.filter__item-btn input[type="hidden"]').val("");
    } else {
      id.find('.filter__item-btn input[type="button"]').val(text);
      id.find('.filter__item-btn input[type="hidden"]').val(dataValue);
    }
  });

  function initializeRateSlider() {
    if ($("#filter__imbd").length) {
      let rateSlider = document.getElementById("filter__imbd");
      let rateValues = [
        document.getElementById("filter__imbd-start"),
        document.getElementById("filter__imbd-end"),
      ];
      let inputRateValues = [
        document.getElementById("imbd-start"),
        document.getElementById("imbd-end"),
      ];

      noUiSlider.create(rateSlider, {
        range: {
          min: 0,
          max: 10,
        },
        step: 0.1,
        connect: true,
        start: [6, 9],
        format: {
          from: function (value) {
            return parseFloat(value).toFixed(1);
          },
          to: function (value) {
            return parseFloat(value).toFixed(1);
          },
        },
      });

      rateSlider.noUiSlider.on("update", function (values, handle) {
        rateValues[handle].innerHTML = values[handle];
        inputRateValues[handle].setAttribute("value", values[handle]);
      });

      $(".filter__item-menu--range").on("click.bs.dropdown", function (e) {
        e.stopPropagation();
        e.preventDefault();
      });
    } else {
      return false;
    }
    return false;
  }
  $(window).on("load", initializeRateSlider());
});
