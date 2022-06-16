from django.contrib.auth.decorators import login_required
from django.urls import include, path

from movies.models import Cast, Comment, Movie, Vote
from movies.views import (
    CastMemberDetailsView,
    ClassicMoviesView,
    CommentView,
    MovieDetailsView,
    MoviesBaseView,
    MoviesByCountryView,
    MoviesByGenreView,
    MoviesByImdbRatingView,
    MoviesMonthView,
    NewMoviesSeriesView,
    PopularMoviesView,
    PopularSeriesView,
    RecentPremieresView,
    VoteView,
    get_filter_countries,
    get_filter_genres,
    get_filter_year,
)

comment_urlpatterns = [
    path(
        "movie/<int:pk>",
        login_required(CommentView.as_view(model=Movie)),
        name="movie_comment",
    ),
    path(
        "cast/<int:pk>",
        login_required(CommentView.as_view(model=Cast)),
        name="cast_comment",
    ),
]

vote_urlpatterns = [
    path(
        "comment/<int:pk>/like",
        login_required(VoteView.as_view(model=Comment, vote_type=Vote.LIKE)),
        name="comment_like",
    ),
    path(
        "comment/<int:pk>/dislike",
        login_required(VoteView.as_view(model=Comment, vote_type=Vote.DISLIKE)),
        name="comment_dislike",
    ),
    path(
        "movie/<int:pk>/like",
        login_required(VoteView.as_view(model=Movie, vote_type=Vote.LIKE)),
        name="movie_like",
    ),
    path(
        "movie/<int:pk>/dislike",
        login_required(VoteView.as_view(model=Movie, vote_type=Vote.DISLIKE)),
        name="movie_dislike",
    ),
    path(
        "cast/<int:pk>/like",
        login_required(VoteView.as_view(model=Cast, vote_type=Vote.LIKE)),
        name="cast_like",
    ),
    path(
        "cast/<int:pk>/dislike",
        login_required(VoteView.as_view(model=Cast, vote_type=Vote.DISLIKE)),
        name="cast_dislike",
    ),
]

filter_urlpatterns = [
    path("countries/", get_filter_countries, name="get_countries"),
    path("years/", get_filter_year, name="get_years"),
    path("genres/", get_filter_genres, name="get_genres"),
]

category_urlpatterns = [
    path(
        "movie/genre/<slug:slug>/",
        MoviesByGenreView.as_view(),
        name="movies_genre_list",
    ),
    path(
        "movie/country/<str:name>/",
        MoviesByCountryView.as_view(),
        name="movies_country_list",
    ),
]

catalogs_urlpatterns = [
    path("imdb-top/", MoviesByImdbRatingView.as_view(), name="imdb-top"),
    path("classic-movies/", ClassicMoviesView.as_view(), name="classic-movies"),
    path("popular-movies/", PopularMoviesView.as_view(), name="popular-movies"),
    path("popular-series/", PopularSeriesView.as_view(), name="popular-series"),
    path("recent-premieres/", RecentPremieresView.as_view(), name="recent-premieres"),
    path("new-movies-series/", NewMoviesSeriesView.as_view(), name="new-movies-series"),
    path("movies-month/", MoviesMonthView.as_view(), name="movies-month"),
]

urlpatterns = [
    path("", MoviesBaseView.as_view(), name="index"),
    path("movie/<int:pk>", MovieDetailsView.as_view(), name="movie_detail"),
    path("series/<int:pk>", MovieDetailsView.as_view(), name="series_detail"),
    path("cast/<int:pk>", CastMemberDetailsView.as_view(), name="cast"),
    # ajax vote
    path("", include(vote_urlpatterns)),
    path("", include(category_urlpatterns)),
    path("comment/", include(comment_urlpatterns)),
    path("filter/", include(filter_urlpatterns)),
    path("catalog/", include(catalogs_urlpatterns)),
]
