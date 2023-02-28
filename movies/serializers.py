from rest_framework.fields import CharField, TimeField
from rest_framework.serializers import ModelSerializer

from movies.models import Cast, Collection, Country, Genre, Movie, StreamingPlatform


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
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


class MovieBaseSerializer(ModelSerializer):
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
            "imdb_link",
            "runtime",
            "release",
            "keywords",
            "box_office",
            "age_mark",
            "awards",
            "is_movie",
            "total_seasons",
        )


class MovieSerializer(MovieBaseSerializer):
    directors = CastSerializer(many=True, read_only=True, required=False)
    writers = CastSerializer(many=True, read_only=True, required=False)
    actors = CastSerializer(many=True, read_only=True, required=False)
    countries = CountrySerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = MovieBaseSerializer.Meta.fields + (
            "countries",
            "genres",
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
