from django_filters import CharFilter, FilterSet, NumberFilter, OrderingFilter

from movies.models import Movie


class MovieFilter(FilterSet):
    year = NumberFilter(field_name="year", lookup_expr="iexact")
    categories = CharFilter(field_name="categories__slug", lookup_expr="iexact")
    genres = CharFilter(field_name="categories__slug", lookup_expr="iexact")

    country = CharFilter(field_name="country", lookup_expr="contains")

    sort_by = OrderingFilter(
        fields={
            ("imdb_rate", "imdb_rate"),
            ("year", "year"),
            ("imdb_votes", "imdb_votes"),
        }
    )

    class Meta:
        model = Movie
        fields = ["country", "year", "categories", "genres", "sort_by"]
