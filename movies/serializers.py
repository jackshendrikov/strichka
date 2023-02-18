from rest_framework.fields import CharField, TimeField
from rest_framework.serializers import ModelSerializer

from movies.models import Cast, Category, Collection, Country, Movie, StreamingPlatform


class CategorySerializer(ModelSerializer):
    class Meta:
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


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ("name", "code")


class MovieSerializer(ModelSerializer):
    runtime = TimeField(
        format="%H:%M", input_formats="%H:%M", required=False, read_only=True
    )
    directors = CastSerializer(many=True, read_only=True)
    writers = CastSerializer(many=True, read_only=True)
    actors = CastSerializer(many=True, read_only=True)
    country = CountrySerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

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
            "imdb_link",
            "runtime",
            "release",
            "keywords",
            "box_office",
            "age_mark",
            "awards",
            "is_movie",
            "total_seasons",
            "country",
            "categories",
            "actors",
            "directors",
            "writers",
        )


class StreamingPlatformSerializer(ModelSerializer):
    movie: CharField = CharField(source="movie.title")

    class Meta:
        model = StreamingPlatform
        fields = ("service", "url", "video_format", "purchase_type", "movie")


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ("name", "background", "movies", "is_active")
