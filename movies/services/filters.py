from django.db.models import QuerySet
from django_filters import (
    BooleanFilter,
    CharFilter,
    FilterSet,
    NumberFilter,
    OrderingFilter,
    TimeFilter,
)

from movies.models import Movie, StreamingPlatform

BASE_FILTER_FIELDS = ["genres", "countries", "year", "imdb_rate", "sort_by"]


class MovieFilter(FilterSet):
    genres = CharFilter(field_name="genres__slug", lookup_expr="iexact")
    countries = CharFilter(field_name="countries__name", lookup_expr="iexact")

    year__gt = NumberFilter(field_name="year", lookup_expr="gte")
    year__lt = NumberFilter(field_name="year", lookup_expr="lte")

    imdb_rate__gt = NumberFilter(field_name="imdb_rate", lookup_expr="gte")
    imdb_rate__lt = NumberFilter(field_name="imdb_rate", lookup_expr="lte")

    platforms = CharFilter(field_name="service", method="filter_platforms")

    sort_by = OrderingFilter(
        fields={
            ("imdb_rate", "imdb_rate"),
            ("year", "year"),
            ("imdb_votes", "imdb_votes"),
        }
    )

    class Meta:
        model = Movie
        fields = BASE_FILTER_FIELDS

    @staticmethod
    def filter_platforms(queryset: QuerySet, name: str, value: str) -> QuerySet:
        platform_movies = StreamingPlatform.objects.filter(**{name: value}).values(
            "movie"
        )
        platform_movies = Movie.objects.filter(id__in=platform_movies).distinct()
        queryset = queryset.distinct()
        return platform_movies & queryset


class AdvancedMovieFilter(MovieFilter):
    is_movie = BooleanFilter(field_name="is_movie")
    age_marks = CharFilter(field_name="age_mark", lookup_expr="iexact")

    imdb_vote__gt = NumberFilter(field_name="imdb_votes", lookup_expr="gte")
    imdb_vote__lt = NumberFilter(field_name="imdb_votes", lookup_expr="lte")

    runtime__gt = TimeFilter(field_name="runtime", lookup_expr="gte")
    runtime__lt = TimeFilter(field_name="runtime", lookup_expr="lte")

    keywords = CharFilter(field_name="keywords", lookup_expr="icontains")
    cast = CharFilter(field_name="actors__full_name", lookup_expr="icontains")

    class Meta:
        fields = BASE_FILTER_FIELDS + [
            "is_movie",
            "age_mark",
            "runtime",
            "keywords",
            "actors",
        ]


class SearchFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Movie
        fields = ["title"]
