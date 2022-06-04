from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from movies.models import Cast, Category, Collection, Movie, StreamingPlatform


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ("slug", "name", "created_at", "updated_at")
        export_order = fields


class CastResource(resources.ModelResource):
    class Meta:
        model = Cast
        fields = (
            "full_name",
            "description",
            "birthday",
            "photo",
            "movies_num",
            "created_at",
            "updated_at",
        )
        export_order = fields


class MovieResource(resources.ModelResource):
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
            "genres",
            "imdb_link",
            "runtime",
            "release",
            "keywords",
            "country",
            "box_office",
            "age_mark",
            "awards",
            "is_movie",
            "total_seasons",
            "created_at",
            "updated_at",
        )
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
        skip_diff = True
        import_id_fields = fields
        export_order = fields


class CollectionResource(resources.ModelResource):
    class Meta:
        model = Collection
        fields = ("name", "is_active", "created_at", "updated_at")
        export_order = fields
