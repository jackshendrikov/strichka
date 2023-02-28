import re
from datetime import date, timedelta
from pydantic import BaseModel, HttpUrl, validator

from movies.models import Cast, Collection, Country, Genre, Movie


class GenreSchema(BaseModel):
    """
    Genre schema.
    """

    name: str
    slug: str

    @validator("name")
    def genre_exist(cls, name: str) -> str:
        if Genre.objects.filter(name=name).exists():
            raise ValueError(f"Genre: `{name}` already exist.")
        return name


class CastSchema(BaseModel):
    """
    Cast schema.
    """

    imdb_id: str
    full_name: str
    description: str | None = None
    birthday: date | None = None
    place_of_birth: str | None = None
    photo: HttpUrl

    @validator("imdb_id")
    def imdb_id_validation(cls, imdb_id: str) -> str:
        if not re.match(r"^nm\d+$", imdb_id):
            raise ValueError(f"Wrong IMBD ID format: `{imdb_id}`")

        if Cast.objects.filter(imdb_id=imdb_id).exists():
            raise ValueError(f"Actor with ID: `{imdb_id}` already exist.")
        return imdb_id


class CountrySchema(BaseModel):
    """
    Country schema.
    """

    name: str
    code: str

    @validator("name")
    def country_exist(cls, name: str) -> str:
        if Country.objects.filter(name=name.lower()).exists():
            raise ValueError(f"Country: `{name}` already exist.")
        return name

    @validator("code")
    def code_exist(cls, code: str) -> str:
        if Country.objects.filter(code=code).exists():
            raise ValueError(f"Country code: `{code}` already exist.")
        return code


class MovieSchema(BaseModel):
    """
    Movie schema.
    """

    imdb_id: str
    title: str
    plot: str
    year: int
    poster: HttpUrl

    imdb_rate: float
    imdb_votes: int
    imdb_link: HttpUrl

    runtime: timedelta | None = None
    release: date | None = None
    keywords: str = ""

    box_office: int | None = None
    age_mark: str | None = None
    awards: str | None = None
    total_seasons: int | None = None

    is_movie: bool
    trailer_id: str

    genres: list[GenreSchema]
    countries: list[CountrySchema]

    actors: list[CastSchema] | None = None
    directors: list[CastSchema] | None = None
    writers: list[CastSchema] | None = None

    @validator("imdb_id")
    def imdb_id_validation(cls, imdb_id: str) -> str:
        if not re.match(r"^tt\d+$", imdb_id):
            raise ValueError(f"Wrong IMBD ID format: `{imdb_id}`")

        if Movie.objects.filter(imdb_id=imdb_id).exists():
            raise ValueError(f"Movie with ID: `{imdb_id}` already exist.")
        return imdb_id

    @validator("imdb_rate")
    def imdb_rate_validation(cls, imdb_rate: float) -> float:
        if 0 < imdb_rate < 10:
            return imdb_rate
        raise ValueError(f"IMDB rate has an invalid value: `{imdb_rate}`.")


class StreamingPlatformSchema(BaseModel):
    """
    Streaming Platform schema.
    """

    service: str
    url: HttpUrl
    video_format: str
    purchase_type: str
    movie: str


class CollectionSchema(BaseModel):
    """
    Collection schema.
    """

    name: str
    movies: list[str]
    is_active: bool

    @validator("name")
    def collection_exist(cls, name: str) -> str:
        if Collection.objects.filter(name=name).exists():
            raise ValueError(f"Collection with name: `{name}` already exist.")
        return name
