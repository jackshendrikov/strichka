from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.http import HttpRequest

from accounts.models import Profile
from common.admin.base import StrichkaBaseModelAdmin
from common.mixins.export import CustomExportMixin
from common.mixins.export_import import CustomImportExportMixin
from common.mixins.forms import PreservePreviousFormInputsMixin
from movies.models import (
    Cast,
    Collection,
    Comment,
    Country,
    Genre,
    Movie,
    Rating,
    StreamingPlatform,
    Vote,
)
from movies.resources import (
    CastResource,
    CollectionResource,
    CountryResource,
    GenreResource,
    MovieResource,
    StreamingPlatformResource,
)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_select_related = ("profile",)

    def get_inline_instances(
        self, request: HttpRequest, obj: User | None = None
    ) -> list:
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Genre)
class GenreAdmin(CustomExportMixin, StrichkaBaseModelAdmin):
    resource_class = GenreResource

    list_display = ("name", "slug") + StrichkaBaseModelAdmin.list_display  # type: ignore
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(Cast)
class CastAdmin(CustomExportMixin, StrichkaBaseModelAdmin):
    resource_class = CastResource
    list_per_page = 50

    list_display = (
        "imdb_id",
        "full_name",
        "description",
        "birthday",
        "place_of_birth",
        "photo",
    ) + StrichkaBaseModelAdmin.list_display  # type: ignore
    search_fields = ("imdb_id", "full_name")
    ordering = ("-created_at",)


@admin.register(Country)
class CountryAdmin(CustomExportMixin, StrichkaBaseModelAdmin):
    resource_class = CountryResource

    list_display = ("name", "code") + StrichkaBaseModelAdmin.list_display  # type: ignore
    list_editable = ("code",)
    search_fields = ("name", "code")
    ordering = ("-created_at",)


@admin.register(Movie)
class MovieAdmin(
    PreservePreviousFormInputsMixin, CustomImportExportMixin, StrichkaBaseModelAdmin
):
    resource_class = MovieResource
    list_per_page = 50

    preserve_inputs_fields = {"countries", "age_mark", "is_movie"}

    raw_id_fields = ("countries", "actors", "directors", "writers", "genres")

    list_display = (
        "imdb_id",
        "title",
        "year",
        "imdb_rate",
        "imdb_votes",
        "release",
        "plot",
        "get_genres",
        "get_countries",
        "get_actors",
        "get_directors",
        "get_writers",
        "poster",
        "imdb_link",
        "runtime",
        "keywords",
        "box_office",
        "age_mark",
        "awards",
        "is_movie",
        "total_seasons",
    ) + StrichkaBaseModelAdmin.list_display  # type: ignore
    list_filter = ("year", "age_mark", "is_movie")
    list_editable = ("title", "runtime", "keywords", "age_mark", "is_movie")
    search_fields = ("imdb_id", "title", "year")
    ordering = ["-release", "-imdb_votes", "-imdb_rate"]

    @admin.display(description="Genres")
    def get_genres(self, obj: Movie) -> str:
        return ",".join([m.name for m in obj.genres.all()])

    @admin.display(description="Countries")
    def get_countries(self, obj: Movie) -> str:
        return ",".join([m.name for m in obj.countries.all()])

    @admin.display(description="Actors")
    def get_actors(self, obj: Movie) -> str:
        return ",".join([m.full_name for m in obj.actors.all()])

    @admin.display(description="Directors")
    def get_directors(self, obj: Movie) -> str:
        return ",".join([m.full_name for m in obj.directors.all()])

    @admin.display(description="Writers")
    def get_writers(self, obj: Movie) -> str:
        return ",".join([m.full_name for m in obj.writers.all()])


@admin.register(StreamingPlatform)
class StreamingPlatformAdmin(
    PreservePreviousFormInputsMixin, CustomExportMixin, StrichkaBaseModelAdmin
):
    resource_class = StreamingPlatformResource
    list_per_page = 100

    preserve_inputs_fields = {"service", "video_format", "purchase_type"}

    list_display = (
        "movie",
        "service",
        "url",
        "video_format",
        "purchase_type",
    ) + StrichkaBaseModelAdmin.list_display  # type: ignore
    list_filter = ("service", "video_format", "purchase_type")
    list_editable = ("url", "video_format", "purchase_type")
    search_fields = ("service", "movie__title")
    ordering = ("-service",)


@admin.register(Collection)
class CollectionAdmin(CustomExportMixin, StrichkaBaseModelAdmin):
    resource_class = CollectionResource

    list_display = ("name", "is_active") + StrichkaBaseModelAdmin.list_display  # type: ignore
    raw_id_fields = ("movies",)
    search_fields = ("name",)
    ordering = ("-created_at",)


admin.site.register(Rating)
admin.site.register(Vote)
admin.site.register(Comment)
