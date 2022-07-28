function handleFavWatch(item, itemClass) {
  let url = item.attr("data-url");
  let csrf = item.attr("data-csrf_token");

  $.ajax({
    url: url,
    type: "POST",
    data: {
      csrfmiddlewaretoken: csrf,
    },

    success: function (response) {
      item.toggleClass(itemClass);
    },
  });

  return false;
}
