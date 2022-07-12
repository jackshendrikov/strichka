function handleFav() {
    let favorite = $("#favorite");
    let url = favorite.data('url');
    let csrf = favorite.data('csrf_token');

    $.ajax({
        url : url,
        type : 'POST',
        data : {
            'csrfmiddlewaretoken': csrf
        },

        success : function (response) {
            favorite.toggleClass("liked");
        }
    });

    return false;
}


$('#favorite').click(function() {
    handleFav()
});
