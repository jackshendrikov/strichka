from typing import Any

from django.db.models import QuerySet
from rest_framework.fields import CharField, TimeField
from rest_framework.serializers import ListSerializer, ModelSerializer

from movies.models import Cast, Category, Collection, Movie, StreamingPlatform


class FilterCategoryListSerializer(ListSerializer):
    def to_representation(self, data: QuerySet) -> Any:
        data = data.exclude(parent__slug="genres").exclude(slug="genres")
        return super().to_representation(data)


class CategorySerializer(ModelSerializer):
    class Meta:
        list_serializer_class = FilterCategoryListSerializer
        model = Category
        fields = ("name", "slug")


class CastSerializer(ModelSerializer):
    class Meta:
        model = Cast
        fields = (
            "imdb_id",
            "full_name",
            "description",
            "birthday",
            "place_of_birth",
            "photo",
        )


class MovieSerializer(ModelSerializer):
    runtime = TimeField(
        format="%H:%M", input_formats="%H:%M", required=False, read_only=True
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
            "categories",
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
        )


class StreamingPlatformSerializer(ModelSerializer):
    movie: CharField = CharField(source="movie.title")

    class Meta:
        model = StreamingPlatform
        fields = ("service", "url", "video_format", "purchase_type", "movie")


class CollectionSerializer(ModelSerializer):
    movies = CastSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ("name", "movies", "is_active")