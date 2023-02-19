from typing import Any

from cacheops import cached
from django.db.models import QuerySet
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from django_filters.views import FilterView

from common.views import BaseView, is_ajax
from config.settings.base import SESSION_LONG_CACHE_TTL, SESSION_SPECIAL_CACHE_TTL
from movies.models import Cast, Collection, Movie
from movies.services import services
from movies.services.filters import AdvancedMovieFilter, MovieFilter, SearchFilter


def error_403(
    request: HttpRequest, exception: type[Exception] | None = None
) -> HttpResponse:
    return render(request, "errors/403.html")


def error_404(request: HttpRequest, exception: type[Exception]) -> HttpResponse:
    return render(request, "errors/404.html", {})


def error_500(
    request: HttpRequest, exception: type[Exception] | None = None
) -> HttpResponse:
    return render(request, "errors/500.html", {})


class MoviesBaseView(BaseView):
    """
    The main page of the "Search Movies" site, only the most important is displayed.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "index_slider_movies": services.get_movies_slider(limit=12),
            "best_movies": services.get_top_fantasy(limit=3),
            "new_releases": services.get_recent_premieres(limit=18),
            "popular_movies": services.get_popular_movies(limit=18),
            "popular_series": services.get_popular_series(limit=18),
            "cinema_movies": services.get_cinema_movies(limit=6),
        }
        return render(request, "movies/index.html", context)


class AdvancedSearchView(BaseView):
    """Page for advanced search of movies."""

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "movies/adv_search.html")


class MovieDetailsView(BaseView):
    """Detailed information about the movie."""

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        movie = get_object_or_404(Movie, pk=pk)
        context = {"movie": movie.pk}
        context.update(
            {"user": request.user.id if request.user.is_authenticated else -1}  # type: ignore
        )
        context = services.GetMovieDetail.execute(context)
        return render(request, "movies/movie_detail.html", context)


class CastMemberDetailsView(BaseView):
    """Detailed information about cast members."""

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        cast_member = get_object_or_404(Cast, pk=pk)
        context = services.GetCastDetail.execute({"member": cast_member.pk})
        return render(request, "movies/cast_detail.html", context)


class CollectionsView(BaseView):
    """Detailed information about collections."""

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"collections": services.get_collections()}
        return render(request, "movies/collection.html", context)


class RandomMovieView(BaseView):
    """Detailed information about random movie."""

    def get(self, request: HttpRequest) -> HttpResponse:
        movie = services.get_random_movie()
        context = {"movie": movie.pk}
        context.update(
            {"user": request.user.id if request.user.is_authenticated else -1}  # type: ignore
        )
        context = services.GetMovieDetail.execute(context)
        return render(request, "movies/movie_detail.html", context)


class AddFavoriteMovieView(View):
    """Add movie in User favorite list."""

    def post(self, request: HttpRequest, pk: int) -> HttpResponse | None:
        if is_ajax(request=request):
            services.add_favorite_movie(movie_id=pk, user_id=request.user.pk)
            return HttpResponse("success")


class AddWatchlistMovieView(View):
    """Add movie in User watchlist."""

    def post(self, request: HttpRequest, pk: int) -> HttpResponse | None:
        if is_ajax(request=request):
            services.add_watchlist_movie(movie_id=pk, user_id=request.user.pk)
            return HttpResponse("success")


class MoviesOfCollectionView(FilterView):
    """Displaying a list of movies of a certain collection."""

    filterset_class = MovieFilter
    paginate_by = 30
    template_name = "movies/movie_list.html"

    def get_collection(self) -> Collection:
        return get_object_or_404(Collection, pk=self.kwargs["pk"])

    @cached(timeout=SESSION_SPECIAL_CACHE_TTL)
    def get_queryset(self) -> QuerySet:
        collection = self.get_collection()
        queryset = services.get_movies_of_collection(collection=collection)
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        collection = self.get_collection()
        context["page_title"] = f"{collection.name} Collection"
        return context


class FilteredListView(FilterView):
    """Base view for specific movie collection pages."""

    page_title = ""
    filterset_class = MovieFilter
    paginate_by = 18
    template_name = "movies/movie_list.html"

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title
        context["objects_len"] = len(self.object_list)
        return context


class AllMoviesView(FilteredListView):
    """All movies view"""

    page_title = "All Movies"

    @cached(timeout=SESSION_LONG_CACHE_TTL)
    def get_queryset(self) -> QuerySet:
        return services.get_all_movies()


class SearchMovieView(FilteredListView):
    """Search movie view."""

    page_title = "Search Result"
    filterset_class = SearchFilter
    paginate_by = 30

    def get_queryset(self) -> QuerySet | None:
        search_request = self.request.GET

        if search_request:
            if ("q" in search_request) and search_request["q"].strip():
                try:
                    return services.search_movie(title=search_request["q"].strip())
                except ValueError:
                    raise Http404()

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context["hide_filters"] = True
        return context


class AdvancedSearchResultView(AllMoviesView):
    """Page for result of advanced search of movies."""

    page_title = "Search Results"
    filterset_class = AdvancedMovieFilter

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context["hide_filters"] = True
        return context


class MoviesByYearView(FilteredListView):
    """
    List of movies released in specific year or in the range of years.
    """

    page_title = "Movies by Year"

    @cached(timeout=SESSION_LONG_CACHE_TTL)
    def get_queryset(self) -> QuerySet:
        self.page_title = f"{self.page_title} ({self.kwargs['year']})"
        try:
            queryset = services.get_movies_list_by_years(self.kwargs["year"])
        except ValueError:
            raise Http404()

        return queryset


class MoviesByCountryView(FilteredListView):
    """List of movies released in specific country."""

    page_title = "Movies by Country"

    @cached(timeout=SESSION_LONG_CACHE_TTL)
    def get_queryset(self) -> QuerySet:
        self.page_title = f"{self.page_title} ({self.kwargs['name']})"
        try:
            queryset = services.get_movies_list_by_country(self.kwargs["name"])
        except ValueError:
            raise Http404()

        return queryset


class MoviesByGenreView(FilteredListView):
    """List of movies in specific genre."""

    page_title = "Movies by Genre"

    @cached(timeout=SESSION_LONG_CACHE_TTL)
    def get_queryset(self) -> QuerySet:
        self.page_title = f"{self.page_title} ({self.kwargs['slug'].title()})"
        try:
            queryset = services.get_movies_list_by_genre(self.kwargs["slug"])
        except ValueError:
            raise Http404()

        return queryset


class MoviesByImdbRatingView(FilteredListView):
    """Top list of movies and series according to IMDB."""

    page_title = "Movies by IMDB Rate"
    queryset = services.get_imdb_top()


class ClassicMoviesView(FilteredListView):
    """Top classic movies."""

    page_title = "TOP Classic movies"
    queryset = services.get_top_classics(limit=300)


class PopularMoviesView(FilteredListView):
    """List of popular movies."""

    page_title = "Popular movies"
    queryset = services.get_popular_movies(limit=300)


class PopularSeriesView(FilteredListView):
    """List of popular series."""

    page_title = "Popular series"
    queryset = services.get_popular_series(limit=300)


class RecentPremieresView(FilteredListView):
    """Recent movie and series premieres."""

    page_title = "Recent premieres"
    queryset = services.get_recent_premieres(limit=100)


class NewMoviesSeriesView(FilteredListView):
    """New movies and series."""

    page_title = "New movies"
    queryset = services.get_new_movies_and_series(limit=150)


class MoviesMonthView(FilteredListView):
    """List movies of the month."""

    page_title = "Movies of the Month"
    queryset = services.get_movie_of_month()


def get_filter_countries(request: HttpRequest) -> JsonResponse | None:
    """Get all the countries from the DB."""

    if request.method == "GET" and is_ajax(request=request):
        countries = services.DataFilters.get_countries()
        data = {"countries": countries}
        return JsonResponse(data, status=200)


def get_filter_year(request: HttpRequest) -> JsonResponse | None:
    """Get all the years from the DB."""

    if request.method == "GET" and is_ajax(request=request):
        years = services.DataFilters.get_years()
        data = {"years": years}
        return JsonResponse(data, status=200)


def get_filter_genres(request: HttpRequest) -> JsonResponse | None:
    """Get all the genres from the DB."""

    if request.method == "GET" and is_ajax(request=request):
        genres = services.DataFilters.get_genres()
        data = {"genres": genres}
        return JsonResponse(data, status=200)


def get_filter_imdb_votes(request: HttpRequest) -> JsonResponse | None:
    """Get IMDb votes from the DB."""

    if request.method == "GET" and is_ajax(request=request):
        imdb_votes = services.DataFilters.get_imdb_votes()
        data = {"imdb_votes": imdb_votes}
        return JsonResponse(data, status=200)


def get_filter_age_mark(request: HttpRequest) -> JsonResponse | None:
    """Get age marks from the DB."""

    if request.method == "GET" and is_ajax(request=request):
        age_marks = services.DataFilters.get_age_marks()
        data = {"age_marks": age_marks}
        return JsonResponse(data, status=200)


def get_filter_platforms(request: HttpRequest) -> JsonResponse | None:
    """Get all the platforms from the DB."""

    if request.method == "GET" and is_ajax(request=request):
        platforms = services.DataFilters.get_platforms()
        data = {"platforms": platforms}
        return JsonResponse(data, status=200)


class CommentView(View):
    """Adding comments to movies and series."""

    model: Movie | Cast | None = None

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        _mutable = request.POST._mutable  # noqa: WPS122
        request.POST._mutable = True  # type: ignore
        request.POST["user"] = request.user  # type: ignore
        request.POST._mutable = _mutable  # noqa: WPS121

        obj: Movie | Cast = get_object_or_404(self.model, pk=pk)  # type: ignore
        services.add_comment(post_request=request.POST, obj=obj)
        return redirect(f"{obj.get_absolute_url()}#comments")


class VoteView(View):
    """Like/Dislike system."""

    model: Movie | Cast | None = None
    vote_type: int | None = None

    def post(self, request: HttpRequest, pk: int) -> HttpResponse | None:
        obj: Movie | Cast = get_object_or_404(self.model, pk=pk)  # type: ignore
        if is_ajax(request=request):
            context = services.add_vote(
                user=request.user, vote_type=self.vote_type, obj=obj
            )
            return JsonResponse(context)


class RatingView(View):
    """Rating system."""

    model: Movie | None = None

    def post(self, request: HttpRequest, pk: int) -> HttpResponse | None:
        obj: Movie = get_object_or_404(self.model, pk=pk)  # type: ignore
        if is_ajax(request=request):
            context = services.add_rate(
                user=request.user,
                rate_value=self.request.POST.get("rate_value", None),  # type: ignore
                obj=obj,
            )
            return JsonResponse(context)
