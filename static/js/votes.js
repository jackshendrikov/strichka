function like() {
  let like = $(this);
  let pk = like.data("id");
  let url = like.data("url");
  let csrf = like.data("csrf_token");

  $.ajax({
    url: url,
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf,
    },

    success: function (json) {
      $("#like" + pk).text(json.like_count);
      $("#dislike" + pk).text(json.dislike_count);
    },
  });

  return false;
}

function dislike() {
  let dislike = $(this);
  let pk = dislike.data("id");
  let csrf = dislike.data("csrf_token");
  let url = dislike.data("url");

  $.ajax({
    url: url,
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf,
    },

    success: function (json) {
      $("#dislike" + pk).text(json.dislike_count);
      $("#like" + pk).text(json.like_count);
    },
  });

  return false;
}

$(function () {
  $('[data-action="like"]').click(like);
  $('[data-action="dislike"]').click(dislike);
});
