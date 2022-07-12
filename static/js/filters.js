$(document).ready(function() {
    getGenres();
    getCountries();
    getYears();
    getPlatforms();
})

function getGenres() {
    let url = $("#genres").attr("url");

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function(result) {
            let genres_option = "<li data-value=''>Any Genre</li>";
            $.each(result["genres"], function(a, b) {
                genres_option += `<li data-value='${b["categories__slug"]}'>${b["categories__name"]}</li>`
            });
            $("#genres").html(genres_option)
        },
        error: function(response) {
            console.log(response)
        },
        async: false
    });
}

function getCountries() {
    let url = $("#countries").attr("url");

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function(result) {
            let countries_option = "<li data-value=''>Any Country</li>";
            $.each(result["countries"], function(a, b) {
                countries_option += `<li data-value='${b["country__name"]}'>${b["country__name"]} (${b["country__code"]})</li>`
            });
            $("#countries").html(countries_option)
        },
        error: function(response) {
            console.log(response)
        },
        async: false
    });
}

function getYears() {
    let url = $("#years").attr("url");

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function(result) {
            let yearSlider = document.getElementById('filter__years');
            noUiSlider.create(yearSlider, {
                range: {
                    'min': result["years"][0],
                    'max': result["years"][1]
                },
                step: 1,
                connect: true,
                start: [2000, new Date().getFullYear()],
                format: {
                    from: function(value) {
                        return parseInt(value);
                    },
                    to: function(value) {
                        return parseInt(value);
                    }
                }
            });
            let yearValues = [
                document.getElementById('filter__years-start'),
                document.getElementById('filter__years-end')
            ];
            let inputYearValues = [
                document.getElementById('years-start'),
                document.getElementById('years-end')
            ];
            yearSlider.noUiSlider.on('update', function(values, handle) {
                yearValues[handle].innerHTML = values[handle];
                inputYearValues[handle].setAttribute("value", values[handle]);
            });
        },
        error: function(response) {
            console.log(response)
        },
        async: false
    });
}

function getPlatforms() {
    let url = $("#platforms").attr("url");

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function(result) {
            let platforms_option = "<li data-value=''>Any Platform</li>";
            $.each(result["platforms"], function(a, b) {
                platforms_option += `<li data-value='${b["service"]}'>${b["service"]}</li>`
            });
            $("#platforms").html(platforms_option)
        },
        error: function(response) {
            console.log(response)
        },
        async: false
    });
}
