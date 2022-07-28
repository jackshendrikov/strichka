$(document).ready(function () {
  "use strict";

  const convertMinsToHrsMins = (mins) => {
    let h = Math.floor(mins / 60);
    let m = mins % 60;
    h = h < 10 ? "0" + h : h;
    m = m < 10 ? "0" + m : m;
    return `${h}:${m}`;
  };

  function initializeRuntimeSlider() {
    if ($("#filter__runtime").length) {
      let runtimeSlider = document.getElementById("filter__runtime");
      let runtimeValues = [
        document.getElementById("filter__runtime-start"),
        document.getElementById("filter__runtime-end"),
      ];
      let inputRuntimeValues = [
        document.getElementById("runtime-start"),
        document.getElementById("runtime-end"),
      ];

      noUiSlider.create(runtimeSlider, {
        range: {
          min: 0,
          max: 240,
        },
        step: 10,
        connect: true,
        start: [0, 150],
        format: {
          from: function (value) {
            return parseInt(value, 10);
          },
          to: function (value) {
            return parseInt(value, 10);
          },
        },
      });

      runtimeSlider.noUiSlider.on("update", function (values, handle) {
        runtimeValues[handle].innerHTML = values[handle];
        inputRuntimeValues[handle].setAttribute(
          "value",
          convertMinsToHrsMins(values[handle])
        );
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
  $(window).on("load", initializeRuntimeSlider());
});
