function rate() {
  let rating = $(this);
  let url = rating.data("url");
  let value = rating.data("value");
  let csrf = rating.data("csrf_token");

  $.ajax({
    url: url,
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf,
      rate_value: value,
    },

    success: function (json) {
      let rateValue = json.result_value;
      if (rateValue) {
        $("#exclude-rating").css("display", "flex");
        $("#rating-" + rateValue).prop("checked", true);
        $("#movie-card-rating-button").html(
          '<span><i class="icon ion-md-star"></i>&nbsp;' +
            rateValue +
            " / 10</span>"
        );
      } else {
        $(".rating-star").prop("checked", false);
        $("#movie-card-rating-button").html(
          '<span><i class="icon ion-md-star-outline"></i>&nbsp;Rate</span>'
        );
      }
    },
  });

  return false;
}

$(function () {
  $('[data-action="rate"]').click(rate);
});
