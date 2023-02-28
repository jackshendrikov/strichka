from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from common.forms import validate_form_with_schema
from common.models.base import StrichkaBaseModel
from movies.services.model_manager import MovieManager, VoteManager


class Genre(StrichkaBaseModel):
    """
    Model to store genres.
    Have a tree structure for convenient use.
    """

    name = models.CharField(
        verbose_name="Genre name", max_length=150, help_text="Genre name"
    )
    slug = models.SlugField(
        verbose_name="Unique ID", max_length=160, unique=True, help_text="Unique ID"
    )

    class Meta:
        verbose_name_plural = "Genres"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("movies_genre_list", kwargs={"slug": self.slug})

    def clean(self) -> None:
        """
        Validate form inputs.
        """
        from movies.schema import GenreSchema
        from movies.serializers import GenreSerializer

        validate_form_with_schema(GenreSchema, GenreSerializer, self)


class Rating(StrichkaBaseModel):
    """
    Model to evaluate movies, series, actors, directors, collections.
    """

    value = models.PositiveSmallIntegerField(
        verbose_name="Rate value", null=True, blank=True, help_text="Rate value"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    object_id = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Ratings"
        unique_together = ("user", "content_type", "object_id")


class Vote(StrichkaBaseModel):
    """
    Model to evaluate comments.
    Serves as an additional layer for evaluating actors, films, etc.
    """

    LIKE = 1
    DISLIKE = -1

    VOTES_CHOICES = ((DISLIKE, "👎"), (LIKE, "👍"))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User"
    )
    vote = models.SmallIntegerField(
        verbose_name="Vote", choices=VOTES_CHOICES, null=True, help_text="Vote value"
    )
    liked_on = models.DateTimeField(auto_now=True, help_text="Liked at")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    object_id = models.PositiveIntegerField(blank=True)

    objects: VoteManager = VoteManager()

    class Meta:
        verbose_name_plural = "Votes"
        unique_together = ("user", "content_type", "object_id")


class Comment(StrichkaBaseModel, MPTTModel):
    """
    Model to store comments on movies, actors, series.
    Have tree structure for convenient use.
    """

    text = models.TextField(verbose_name="Comment text", help_text="Comment text")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")
    object_id = models.PositiveIntegerField()

    votes = GenericRelation(Vote, related_query_name="comment")
    commented_on = models.DateTimeField(
        verbose_name="Published time", auto_now=True, help_text="Comment published time"
    )

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return self.text


class Cast(StrichkaBaseModel):
    """
    Model to store information about movie cast.
    """

    imdb_id = models.CharField(
        verbose_name="IMDB ID",
        max_length=128,
        db_index=True,
        unique=True,
        help_text="IMDB ID of cast member",
    )
    full_name = models.CharField(
        verbose_name="Cast member name", max_length=150, help_text="Cast member name"
    )
    description = models.TextField(
        null=True, blank=True, help_text="Info about cast member"
    )
    birthday = models.DateField(
        verbose_name="Birthday date", null=True, blank=True, help_text="Birthday date"
    )
    place_of_birth = models.CharField(
        verbose_name="Place of birth",
        null=True,
        blank=True,
        max_length=150,
        help_text="Place of birth",
    )
    photo = models.URLField(
        verbose_name="Cast member photo", max_length=220, help_text="Cast member photo"
    )

    comments = GenericRelation(Comment)
    ratings = GenericRelation(Rating)
    votes = GenericRelation(Vote, related_query_name="cast")

    def __str__(self) -> str:
        return self.full_name

    def get_absolute_url(self) -> str:
        return reverse("cast", kwargs={"pk": self.pk})

    def clean(self) -> None:
        """
        Validate form inputs.
        """
        from movies.schema import CastSchema
        from movies.serializers import CastSerializer

        validate_form_with_schema(CastSchema, CastSerializer, self)


class Country(StrichkaBaseModel):
    """
    Model to store countries.
    """

    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=5, unique=True)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("movies_country_list", kwargs={"name": self.name})

    def clean(self) -> None:
        """
        Validate form inputs.
        """
        from movies.schema import CountrySchema
        from movies.serializers import CountrySerializer

        validate_form_with_schema(CountrySchema, CountrySerializer, self)


class Movie(StrichkaBaseModel):
    """
    Model with information about movies and series.
    """

    title = models.CharField(
        verbose_name="Movie title",
        max_length=150,
        db_index=True,
        help_text="Movie title",
    )
    plot = models.TextField(help_text="Movie plot")
    year = models.PositiveSmallIntegerField(verbose_name="Movie release year")
    poster = models.URLField(max_length=220, help_text="Movie poster")

    imdb_id = models.CharField(
        max_length=128, db_index=True, unique=True, help_text="Movie IMDB ID"
    )
    imdb_link = models.URLField(max_length=220, help_text="Movie IMDB link")
    imdb_rate = models.FloatField(verbose_name="IMDB Rate", help_text="IMDB Rate")
    imdb_votes = models.PositiveIntegerField(
        verbose_name="IMDB Votes", help_text="IMDB Votes"
    )

    runtime = models.TimeField(
        verbose_name="Movie duration", null=True, blank=True, help_text="Movie runtime"
    )
    release = models.DateField(
        verbose_name="Release date", null=True, blank=True, help_text="Release date"
    )
    keywords = models.TextField(null=True, blank=True, help_text="Movie keywords")
    box_office = models.BigIntegerField(
        verbose_name="Movie fees in the world",
        null=True,
        blank=True,
        help_text="Movie fees in the world",
    )
    age_mark = models.CharField(
        verbose_name="Age mark", max_length=16, help_text="Movie age rate"
    )
    awards = models.TextField(null=True, blank=True, help_text="Movie awards")
    trailer_id = models.CharField(
        max_length=20, unique=True, null=True, blank=True, help_text="Movie trailer ID"
    )

    is_movie = models.BooleanField(default=True, help_text="Movie type (Movie/Series)")
    total_seasons = models.PositiveSmallIntegerField(
        verbose_name="Total seasons of series", null=True, blank=True
    )

    directors = models.ManyToManyField(Cast, related_name="movie_directors", blank=True)
    writers = models.ManyToManyField(Cast, related_name="movie_writers", blank=True)
    actors = models.ManyToManyField(Cast, related_name="movie_actors", blank=True)

    countries = models.ManyToManyField(Country)
    genres = models.ManyToManyField(Genre)
    comments = GenericRelation(Comment)
    ratings = GenericRelation(Rating)
    votes = GenericRelation(Vote, related_query_name="movie")

    objects: MovieManager = MovieManager()

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"

    def get_absolute_url(self) -> str:
        if self.is_movie:
            return reverse("movie_detail", kwargs={"pk": self.pk})
        return reverse("series_detail", kwargs={"pk": self.pk})

    def keywords_as_list(self) -> list[str]:
        return self.keywords.split(",") if self.keywords else []

    def clean(self) -> None:
        """
        Validate form inputs.
        """
        from movies.schema import MovieSchema
        from movies.serializers import MovieBaseSerializer

        validate_form_with_schema(MovieSchema, MovieBaseSerializer, self)


class StreamingPlatform(StrichkaBaseModel):
    """
    Models to store movie links to streaming services.
    """

    service = models.CharField(
        verbose_name="Streaming service name",
        max_length=255,
        help_text="Streaming service name",
    )
    url = models.URLField(null=True, blank=True)
    video_format = models.CharField(
        verbose_name="Available video formats",
        max_length=255,
        help_text="Available video formats",
    )
    purchase_type = models.CharField(
        verbose_name="Available purchase types",
        max_length=255,
        help_text="Available purchase types",
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Streaming platform"
        verbose_name_plural = "Streaming platforms"

        unique_together = ("service", "movie")

    def __str__(self) -> str:
        return self.service

    def video_format_as_list(self) -> list[str]:
        return self.video_format.split(",")

    def purchase_type_as_list(self) -> list[str]:
        return self.purchase_type.split(",")

    def clean(self) -> None:
        """
        Validate form inputs.
        """
        from movies.schema import StreamingPlatformSchema
        from movies.serializers import StreamingPlatformSerializer

        validate_form_with_schema(
            StreamingPlatformSchema, StreamingPlatformSerializer, self
        )


class Collection(StrichkaBaseModel):
    """
    Model to store collections of movies.
    """

    name = models.CharField(
        verbose_name="Collection name", max_length=150, help_text="Collection name"
    )
    movies = models.ManyToManyField(
        Movie,
        verbose_name="Movies in collection",
        blank=True,
        related_query_name="collection",
        help_text="Movies in collection",
    )
    background = models.URLField(
        verbose_name="Collection photo",
        max_length=220,
        null=True,
        blank=True,
        help_text="Collection photo",
    )
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Collections"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("movies_collection", kwargs={"pk": self.pk})

    def clean(self) -> None:
        """
        Validate form inputs.
        """
        from movies.schema import CollectionSchema
        from movies.serializers import CollectionSerializer

        validate_form_with_schema(CollectionSchema, CollectionSerializer, self)
