from django.urls import path

from movies.views import MovieDetailsView, MoviesBaseView

urlpatterns = [
    path("", MoviesBaseView.as_view(), name="index"),
    path("movie/<int:pk>", MovieDetailsView.as_view(), name="movie_detail"),
    path("series/<int:pk>", MovieDetailsView.as_view(), name="series_detail"),
]
