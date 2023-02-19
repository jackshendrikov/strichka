from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from movies.models import Cast, Collection, Country, Genre, Movie, StreamingPlatform


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = ("name", "slug", "created_at", "updated_at")
        import_id_fields = fields
        export_order = fields


class CastResource(resources.ModelResource):
    class Meta:
        model = Cast
        fields = (
            "imdb_id",
            "full_name",
            "description",
            "birthday",
            "place_of_birth",
            "photo",
            "created_at",
            "updated_at",
        )
        use_bulk = True
        import_id_fields = fields
        export_order = fields


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        fields = ("name", "code", "created_at", "updated_at")
        export_order = fields


class MovieResource(resources.ModelResource):
    actors = fields.Field(
        attribute="actors",
        widget=ManyToManyWidget(Cast, field="full_name", separator=","),
    )
    writers = fields.Field(
        attribute="writers",
        widget=ManyToManyWidget(Cast, field="full_name", separator=","),
    )
    directors = fields.Field(
        attribute="directors",
        widget=ManyToManyWidget(Cast, field="full_name", separator=","),
    )
    countries = fields.Field(
        attribute="countries",
        widget=ManyToManyWidget(Cast, field="name", separator=","),
    )

    class Meta:
        model = Movie
        fields = (
            "imdb_id",
            "title",
            "year",
            "imdb_rate",
            "imdb_votes",
            "plot",
            "poster",
            "actors",
            "writers",
            "directors",
            "imdb_link",
            "runtime",
            "release",
            "keywords",
            "countries",
            "box_office",
            "age_mark",
            "awards",
            "is_movie",
            "total_seasons",
            "created_at",
            "updated_at",
        )
        use_bulk = True
        import_id_fields = fields
        export_order = fields


class StreamingPlatformResource(resources.ModelResource):
    movie = fields.Field(
        column_name="category",
        attribute="category",
        widget=ForeignKeyWidget(Movie, "title"),
    )

    class Meta:
        model = StreamingPlatform
        fields = (
            "service",
            "url",
            "video_format",
            "purchase_type",
            "movie",
            "created_at",
            "updated_at",
        )
        use_bulk = True
        import_id_fields = fields
        export_order = fields


class CollectionResource(resources.ModelResource):
    class Meta:
        model = Collection
        fields = ("name", "is_active", "created_at", "updated_at")
        export_order = fields
