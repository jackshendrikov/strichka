from django_filters import CharFilter, FilterSet, NumberFilter, OrderingFilter

from movies.models import Movie


class MovieFilter(FilterSet):
    genres = CharFilter(field_name="categories__slug", lookup_expr="iexact")
    country = CharFilter(field_name="country__name", lookup_expr="iexact")

    year__gt = NumberFilter(field_name="year", lookup_expr="gte")
    year__lt = NumberFilter(field_name="year", lookup_expr="lte")

    imdb_rate__gt = NumberFilter(field_name="imdb_rate", lookup_expr="gte")
    imdb_rate__lt = NumberFilter(field_name="imdb_rate", lookup_expr="lte")

    sort_by = OrderingFilter(
        fields={
            ("imdb_rate", "imdb_rate"),
            ("year", "year"),
            ("imdb_votes", "imdb_votes"),
        }
    )

    class Meta:
        model = Movie
        fields = ["country", "imdb_rate", "year", "genres", "sort_by"]
