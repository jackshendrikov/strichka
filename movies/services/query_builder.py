from dataclasses import dataclass
from django.db.models import QuerySet

from movies.models import Movie


@dataclass
class MovieQueryBuilder:
    """Build Movie Queryset"""

    # Possible parameters
    additional_prefetch: list[str] | None = None
    exclude: dict | None = None
    filter_by: dict | None = None
    order_by: list[str] | None = None
    distinct: bool = True
    limit: int | None = None

    # Default values
    movie_default_prefetch = ["genres"]
    movie_default_fields = [
        "id",
        "title",
        "imdb_rate",
        "imdb_votes",
        "poster",
        "plot",
        "age_mark",
        "is_movie",
    ]

    def build_queryset(self) -> QuerySet:
        """Build movie queryset."""

        query = self._form_prefetch_only_queryset()
        query = self._classify_queryset(query=query)
        query = self._clear_queryset(query=query)

        return query

    def _form_prefetch_only_queryset(self) -> QuerySet:
        """Form prefetch queryset and obtain only selected raw fields"""

        fields, prefetch_fields = self._get_fields_to_obtain()
        return Movie.objects.prefetch_related(*prefetch_fields).only(*fields)

    def _classify_queryset(self, query: QuerySet) -> QuerySet:
        """Filter and sort given query"""

        if self.exclude:
            query = query.exclude(**self.exclude)

        if self.filter_by:
            query = query.filter(**self.filter_by)

        if self.order_by:
            query = query.order_by(*self.order_by)

        return query

    def _clear_queryset(self, query: QuerySet) -> QuerySet:
        """Distinct and limit given queryset"""

        if self.distinct:
            query = query.distinct()

        if self.limit:
            query = query[: self.limit]

        return query

    def _get_fields_to_obtain(self) -> tuple[list[str], list[str]]:
        """Get prefetch and raw fields to process in query"""

        prefetch_fields = self.movie_default_prefetch
        if self.additional_prefetch:
            prefetch_fields += self.additional_prefetch

        fields = self.movie_default_fields + prefetch_fields
        return fields, prefetch_fields
