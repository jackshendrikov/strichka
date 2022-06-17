from typing import Any, Union

import locale
import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count, QuerySet, Sum
from django.db.transaction import atomic
from django.forms import ModelChoiceField
from random import choice
from service_objects.services import Service

from movies.forms import CommentForm
from movies.models import (
    Cast,
    Category,
    Collection,
    Comment,
    Movie,
    StreamingPlatform,
    Vote,
)

locale.setlocale(locale.LC_ALL, "")
logger = logging.getLogger(__name__)


class GetMovieDetail(Service):
    """
    Class to process data about movie detail and transmit necessary info to views.
    """

    movie = ModelChoiceField(queryset=Movie.objects.all())

    def process(self) -> dict:
        movie = self.cleaned_data["movie"]

        genres = self._get_genres(movie)
        countries = self._get_countries(movie)
        actors = self._get_actors(movie)
        directors = self._get_directors(movie)
        writers = self._get_writers(movie)
        platforms = self._get_stream_platforms(movie)
        comments = movie.comments.all()
        likes_count = movie.votes.likes().count()
        dislikes_count = movie.votes.dislikes().count()
        movies_to_discover = get_new_movies_and_series(limit=6)

        context = {
            "movie_id": movie.id,
            "title": movie.title,
            "plot": movie.plot,
            "year": movie.year,
            "poster": movie.poster,
            "imdb_id": movie.imdb_id,
            "imdb_link": movie.imdb_link,
            "imdb_rate": movie.imdb_rate,
            "imdb_votes": movie.imdb_votes,
            "runtime": movie.runtime,
            "release": movie.release,
            "keywords": movie.keywords_as_list(),
            "countries": countries,
            "box_office": movie.box_office,
            "trailer_id": movie.trailer_id,
            "age_mark": movie.age_mark,
            "awards": movie.awards,
            "is_movie": movie.is_movie,
            "total_seasons": movie.total_seasons,
            "genres": genres,
            "actors": actors,
            "directors": directors,
            "writers": writers,
            "comments": comments,
            "platforms": platforms,
            "likes_count": likes_count,
            "dislikes_count": dislikes_count,
            "movies_to_discover": movies_to_discover,
        }

        return context

    @staticmethod
    def _get_genres(movie: Movie) -> QuerySet:
        return movie.categories.filter(parent__slug="genres")

    @staticmethod
    def _get_countries(movie: Movie) -> QuerySet:
        return movie.country.all()

    @staticmethod
    def _get_actors(movie: Movie) -> QuerySet:
        return movie.actors.all()

    @staticmethod
    def _get_directors(movie: Movie) -> QuerySet:
        return movie.directors.all()

    @staticmethod
    def _get_writers(movie: Movie) -> QuerySet:
        return movie.writers.all()

    @staticmethod
    def _get_stream_platforms(movie: Movie) -> QuerySet:
        return StreamingPlatform.objects.filter(movie=movie)


class GetCastDetail(Service):
    """
    Class to process data about cast member and transmit necessary info to views.
    """

    member = ModelChoiceField(queryset=Cast.objects.all())

    def process(self) -> dict:
        member = self.cleaned_data["member"]

        comments = member.comments.all()
        likes_count = member.votes.likes().count()
        dislikes_count = member.votes.dislikes().count()

        role_movies = {
            "actor": member.movie_actors,
            "director": member.movie_directors,
            "writer": member.movie_writers,
        }

        role_counter = {
            "actor": member.movie_actors.count(),
            "director": member.movie_directors.count(),
            "writer": member.movie_writers.count(),
        }

        known_for = role_movies[max(role_counter, key=role_counter.get)].order_by(
            "-imdb_votes", "-imdb_rate"
        )[:6]

        context = {
            "member_id": member.id,
            "imdb_id": member.imdb_id,
            "full_name": member.full_name,
            "description": member.description,
            "birthday": member.birthday,
            "place_of_birth": member.place_of_birth,
            "photo": member.photo,
            "movies_actors": role_movies["actor"].all(),
            "movies_directors": role_movies["director"].all(),
            "movie_writers": role_movies["writer"].all(),
            "known_for": known_for,
            "comments": comments,
            "likes_count": likes_count,
            "dislikes_count": dislikes_count,
        }

        return context


class DataFilters:
    """
    Data for the search movie filter.
    """

    @staticmethod
    def get_categories() -> list[dict[str, str]]:
        categories = (
            Category.objects.exclude(parent__slug="genres", slug="genres")
            .order_by("name")
            .values("name", "slug")
            .distinct()
        )

        return list(categories)

    @staticmethod
    def get_years() -> list[int]:
        years = (
            Movie.objects.exclude(year__exact=None)
            .values_list("year", flat=True)
            .order_by("-year")
            .distinct()
        )

        years = sorted(years)

        return [years[0], years[-1]]

    @staticmethod
    def get_countries() -> list[dict[str, str]]:
        countries = (
            Movie.objects.exclude(country__name__exact=None)
            .values("country__name", "country__code")
            .annotate(country_count=Count("country__name"))
            .order_by("-country_count")
            .distinct()
        )

        return list(countries)

    @staticmethod
    def get_genres() -> list[dict[str, str]]:
        genres = (
            Movie.objects.values("categories__name", "categories__slug")
            .annotate(genres_count=Count("categories__name"))
            .order_by("-genres_count")
            .distinct()
        )

        return list(genres)


def get_imdb_top() -> QuerySet:
    """
    Get top movies and series list according to IMDB.
    """
    return Movie.objects.order_by("-imdb_rate", "-imdb_votes").distinct()


def get_movies_slider(limit: int = None) -> QuerySet:
    """
    Get best movies and series for slider on main page (last 6 months).
    """
    slider_movies = Movie.objects.filter(
        release__range=(datetime.today() + relativedelta(months=-6), datetime.today())
    ).order_by("-imdb_rate", "-imdb_votes")

    if limit:
        return slider_movies[:limit]

    return slider_movies


def get_collections() -> QuerySet:
    """
    Get collections of movies+serials for main page.
    """

    return Collection.objects.filter(is_active=True)


def get_movies_of_collection(collection: Collection) -> QuerySet:
    """
    Get all movies from collection.
    """
    movies = collection.movies.all().prefetch_related()
    return movies


def get_popular_movies(limit: int = None) -> QuerySet:
    """
    Get popular movies according to IMDB.
    """
    popular_movies = Movie.objects.filter(
        is_movie=True,
        release__range=(datetime.today() + relativedelta(years=-1), datetime.today()),
        imdb_rate__gte=5,
    ).order_by("-imdb_votes", "-imdb_rate")

    if limit:
        return popular_movies[:limit]

    return popular_movies


def get_popular_series(limit: int = None) -> QuerySet:
    """
    Get popular series according to IMDB.
    """
    popular_series = Movie.objects.filter(
        is_movie=False,
        release__range=(datetime.today() + relativedelta(years=-1), datetime.today()),
        imdb_rate__gte=5,
    ).order_by("-imdb_votes", "-imdb_rate")

    if limit:
        return popular_series[:limit]

    return popular_series


def get_cinema_movies(limit: int = None) -> QuerySet:
    """
    Get movies currently in cinema.
    """
    cinema_movies = Movie.objects.filter(
        is_movie=True,
        release__range=(datetime.today() + relativedelta(months=-1), datetime.today()),
    ).order_by("-imdb_votes", "-imdb_rate")

    if limit:
        return cinema_movies[:limit]

    return cinema_movies


def get_recent_premieres(limit: int = None) -> QuerySet:
    """
    Get recent movies and series premieres.
    """
    new_releases = (
        Movie.objects.filter(
            release__range=(
                datetime.today() + relativedelta(months=-3),
                datetime.today(),
            )
        )
        .order_by("-imdb_votes", "-imdb_rate", "-release")
        .distinct()
    )

    if limit:
        return new_releases[:limit]

    return new_releases


def get_top_classics(limit: int = None) -> QuerySet:
    """
    Get top classic movies and series list according to IMDB.
    """
    best_movies = (
        Movie.objects.exclude(release__gt=datetime.today() + relativedelta(years=-20))
        .exclude(release__isnull=True)
        .order_by("-imdb_votes", "-imdb_rate")
        .distinct()
    )

    if limit:
        return best_movies[:limit]

    return best_movies


def get_top_fantasy(limit: int = None) -> QuerySet:
    """
    Get top fantasy movies and series list according to IMDB.
    """
    best_fantasy = (
        Movie.objects.filter(categories__name="Fantasy")
        .order_by("-imdb_votes", "-imdb_rate")
        .distinct()
    )

    if limit:
        return best_fantasy[:limit]

    return best_fantasy


def get_new_movies_and_series(limit: int = None) -> QuerySet:
    """
    Get new movies and series (during the year).
    """
    new_movies = Movie.objects.filter(
        release__range=(
            datetime.today() + relativedelta(years=-1),
            datetime.today() + relativedelta(months=-2),
        ),
        imdb_rate__gte=5,
        release__isnull=False,
    ).order_by("-imdb_votes", "-imdb_rate", "-release")

    if limit:
        return new_movies[:limit]

    return new_movies


def get_movies_list_by_genre(slug: str) -> QuerySet:
    """
    Get all movies and series of a specific genre.
    """

    return Movie.objects.filter(categories__slug=slug).distinct()


def get_movies_list_by_years(year: int) -> QuerySet:
    """
    Get all movies and series from specific year range.
    """

    return Movie.objects.filter(year=year).distinct()


def get_movies_list_by_country(country: str) -> QuerySet:
    """
    Get all movies and series from specific country.
    """

    return Movie.objects.filter(country__name__exact=country).distinct()


def ger_random_movie() -> Movie:
    pks = Movie.objects.values_list("pk", flat=True)
    random_pk = choice(pks)  # noqa: S311
    return Movie.objects.get(pk=random_pk)


def get_movie_of_month() -> QuerySet:
    """
    Get best movies and series over the past month.
    """
    return (
        Movie.objects.filter(
            votes__liked_on__range=(
                datetime.today() + relativedelta(months=-1),
                datetime.today(),
            ),
            comments__commented_on__range=(
                datetime.today() + relativedelta(months=-1),
                datetime.today(),
            ),
        )
        .annotate(votes_sum=Sum("votes__vote"), comments_count=Count("comments__text"))
        .exclude(votes_sum=None)
        .order_by("-votes_sum", "-comments_count")
        .distinct()
    )


def add_comment(request_post: Any, content_object: Any) -> None:
    """
    Validate and add comment.
    """
    form = CommentForm(request_post)
    if form.is_valid():
        form = form.save(commit=False)
        form.content_object = content_object
        if request_post.get("parent", None):
            form.parent_id = int(request_post.get("parent"))
        form.save()
    else:
        logger.error(form.errors)


@atomic
def add_vote(obj: Union[Movie, Cast, Comment], vote_type: int, user: User) -> dict:
    """
    Add like or dislike.
    If user has already liked or disliked - entry is deleted.
    If user wants to change value -  update.
    """
    try:  # noqa: WPS229
        like_dislike = Vote.objects.get(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id,
            user=user,
        )
        if like_dislike.vote is not vote_type:
            like_dislike.vote = vote_type
            like_dislike.save(update_fields=["vote"])
            result = True
        else:
            like_dislike.delete()
            result = False
    except Vote.DoesNotExist:
        obj.votes.create(user=user, vote=vote_type)
        result = True

    context = {
        "result": result,
        "like_count": obj.votes.likes().count(),
        "dislike_count": obj.votes.dislikes().count(),
    }

    return context
