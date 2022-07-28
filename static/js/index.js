$(document).ready(function () {
  "use strict";

  let indexSlider = $(".index-slider-area-slider");
  indexSlider.owlCarousel({
    dots: false,
    loop: true,
    autoplay: true,
    autoplayTimeout: 6000,
    items: 1,
  });
  indexSlider.on("changed.owl.carousel", function (property) {
    let current = property.item.index;
    let prevRating = $(property.target)
      .find(".owl-item")
      .eq(current)
      .prev()
      .find(".index-slider-area-slide")
      .html();
    let nextRating = $(property.target)
      .find(".owl-item")
      .eq(current)
      .next()
      .find(".index-slider-area-slide")
      .html();
    $(".thumb-prev .index-slider-area-slide").html(prevRating);
    $(".thumb-next .index-slider-area-slide").html(nextRating);
  });
  $(".thumb-next").on("click", function () {
    indexSlider.trigger("next.owl.carousel", [300]);
    return false;
  });
  $(".thumb-prev").on("click", function () {
    indexSlider.trigger("prev.owl.carousel", [300]);
    return false;
  });

  $(".season__bg").owlCarousel({
    animateOut: "fadeOut",
    animateIn: "fadeIn",
    mouseDrag: false,
    touchDrag: false,
    items: 1,
    dots: false,
    loop: true,
    autoplay: false,
    smartSpeed: 600,
    margin: 0,
  });

  $(".season__bg .item").each(function () {
    if ($(this).attr("data-bg")) {
      $(this).css({
        background: "url(" + $(this).data("bg") + ")",
        "background-position": "center center",
        "background-repeat": "no-repeat",
        "background-size": "cover",
      });
    }
  });

  $(".season__carousel").owlCarousel({
    mouseDrag: false,
    touchDrag: false,
    dots: false,
    loop: true,
    autoplay: false,
    smartSpeed: 600,
    margin: 30,
    responsive: {
      0: {
        items: 2,
      },
      576: {
        items: 2,
      },
      768: {
        items: 3,
      },
      992: {
        items: 4,
      },
      1200: {
        items: 4,
      },
    },
  });

  $(".season__nav--next").on("click", function () {
    $(".season__carousel, .season__bg").trigger("next.owl.carousel");
  });
  $(".season__nav--prev").on("click", function () {
    $(".season__carousel, .season__bg").trigger("prev.owl.carousel");
  });

  $(window).on("resize", function () {
    var itemHeight = $(".season__bg").height();
    $(".season__bg .item").css("height", itemHeight + "px");
  });
  $(window).trigger("resize");

  $(".content__mobile-tabs-menu li").each(function () {
    $(this).attr("data-value", $(this).text().toLowerCase());
  });

  $(".content__mobile-tabs-menu li").on("click", function () {
    var text = $(this).text();
    var item = $(this);
    var id = item.closest(".content__mobile-tabs").attr("id");
    $("#" + id)
      .find(".content__mobile-tabs-btn input")
      .val(text);
  });

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
});
