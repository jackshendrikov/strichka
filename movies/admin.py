from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from common.admin.base import StrichkaBaseModelAdmin
from common.mixins.export import CustomExportMixin
from common.mixins.export_import import CustomImportExportMixin
from common.mixins.forms import PreservePreviousFormInputsMixin
from movies.models import (
    Cast,
    Category,
    Collection,
    Comment,
    Country,
    Movie,
    Rating,
    StreamingPlatform,
    Vote,
)
from movies.resources import (
    CastResource,
    CategoryResource,
    CollectionResource,
    CountryResource,
    MovieResource,
    StreamingPlatformResource,
)


@admin.register(Category)
class CategoryAdmin(CustomExportMixin, StrichkaBaseModelAdmin, DjangoMpttAdmin):
    resource_class = CategoryResource

    list_display = ("name", "slug", "parent") + StrichkaBaseModelAdmin.list_display
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(Cast)
class CastAdmin(CustomExportMixin, StrichkaBaseModelAdmin):
    resource_class = CastResource

    list_display = (
        "imdb_id",
        "full_name",
        "description",
        "birthday",
        "place_of_birth",
        "photo",
    ) + StrichkaBaseModelAdmin.list_display
    search_fields = ("imdb_id", "full_name")
    ordering = ("-created_at",)


@admin.register(Country)
class CountryAdmin(CustomExportMixin, StrichkaBaseModelAdmin):
    resource_class = CountryResource

    list_display = ("name", "code") + StrichkaBaseModelAdmin.list_display
    list_editable = ("code",)
    search_fields = ("name", "code")
    ordering = ("-created_at",)


@admin.register(Movie)
class MovieAdmin(
    PreservePreviousFormInputsMixin, CustomImportExportMixin, StrichkaBaseModelAdmin
):
    resource_class = MovieResource
    list_per_page = 50

    preserve_inputs_fields = {"country", "age_mark", "is_movie"}

    raw_id_fields = ("country", "actors", "directors", "writers", "categories")

    list_display = (
        "imdb_id",
        "title",
        "year",
        "imdb_rate",
        "imdb_votes",
        "release",
        "plot",
        "get_countries",
        "get_actors",
        "get_directors",
        "get_writers",
        "poster",
        "genres",
        "imdb_link",
        "runtime",
        "keywords",
        "box_office",
        "age_mark",
        "awards",
        "is_movie",
        "total_seasons",
    ) + StrichkaBaseModelAdmin.list_display
    list_filter = ("year", "country", "age_mark", "is_movie")
    list_editable = ("title", "keywords", "is_movie")
    search_fields = ("imdb_id", "title", "year", "country__name")
    ordering = ["-release", "-imdb_votes", "-imdb_rate"]

    def get_countries(self, obj: Movie) -> str:
        return ",".join([m.name for m in obj.country.all()])

    get_countries.short_description = "Countries"

    def get_actors(self, obj: Movie) -> str:
        return ",".join([m.full_name for m in obj.actors.all()])

    get_actors.short_description = "Actors"

    def get_directors(self, obj: Movie) -> str:
        return ",".join([m.full_name for m in obj.directors.all()])

    get_directors.short_description = "Directors"

    def get_writers(self, obj: Movie) -> str:
        return ",".join([m.full_name for m in obj.writers.all()])

    get_writers.short_description = "Writers"


@admin.register(StreamingPlatform)
class StreamingPlatformAdmin(
    PreservePreviousFormInputsMixin, CustomExportMixin, StrichkaBaseModelAdmin
):
    resource_class = StreamingPlatformResource

    preserve_inputs_fields = {"service", "video_format", "purchase_type"}

    list_display = (
        "movie",
        "service",
        "url",
        "video_format",
        "purchase_type",
    ) + StrichkaBaseModelAdmin.list_display
    list_filter = ("service", "video_format", "purchase_type")
    list_editable = ("url", "video_format", "purchase_type")
    search_fields = ("service", "movie__title")
    ordering = ("-service",)


@admin.register(Collection)
class CollectionAdmin(CustomExportMixin, StrichkaBaseModelAdmin):
    resource_class = CollectionResource

    list_display = ("name", "is_active") + StrichkaBaseModelAdmin.list_display
    raw_id_fields = ("movies",)
    search_fields = ("name",)
    ordering = ("-created_at",)


admin.site.register(Rating)
admin.site.register(Vote)
admin.site.register(Comment)
