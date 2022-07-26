from enum import Enum


class PlatformCountry(Enum):
    UA = "Ukraine"
    GL = "Global"
    US = "USA"


class Platforms(Enum):
    NETFLIX = "Netflix"
    MEGOGO = "Megogo"
    KYIVSTAR = "Kyivstar TV"
    UAKINO = "UAkino"
    YOUTUBE = "YouTube TV"
    DISNEY = "Disney+"
    HBO_MAX = "HBO MAX"
    AMAZON_PRIME = "Amazon Prime"
    APPLE_TV = "AppleTV+"
    HULU = "Hulu"
    PEACOCK = "Peacock"
    ITUNES = "iTunes"
    AMAZON = "Amazon"
    GOOGLE_PLAY = "Google Play"
    MICROSOFT_STORE = "Microsoft Store"
    PARAMOUNT = "Paramount+"
    AMC = "AMC"
    CBS = "CBS"
    FOX = "FOX"
    THE_CW = "The CW"
    SHUDDER = "Shudder"
    SYFY = "Syfy"
    ADULT_SWIM = "Adult Swim"
    POPCORNFLIX = "Popcornflix"
    FLIXFLING = "FlixFling"
    MUBI = "MUBI"
    VUDU = "VUDU"
    FREEFORM = "Freeform"
    PLUTO_TV = "Pluto TV"
    TUBI_TV = "Tubi TV"


COUNTRY_PLATFORMS_MAP = {
    PlatformCountry.UA.value: [
        Platforms.MEGOGO.value,
        Platforms.KYIVSTAR.value,
        Platforms.UAKINO.value,
    ],
    PlatformCountry.GL.value: [
        Platforms.NETFLIX.value,
        Platforms.YOUTUBE.value,
        Platforms.APPLE_TV.value,
        Platforms.ITUNES.value,
        Platforms.MICROSOFT_STORE.value,
        Platforms.ADULT_SWIM.value,
        Platforms.FLIXFLING.value,
        Platforms.MUBI.value,
    ],
    PlatformCountry.US.value: [
        Platforms.DISNEY.value,
        Platforms.HBO_MAX.value,
        Platforms.AMAZON_PRIME.value,
        Platforms.HULU.value,
        Platforms.PEACOCK.value,
        Platforms.AMAZON.value,
        Platforms.GOOGLE_PLAY.value,
        Platforms.PARAMOUNT.value,
        Platforms.AMC.value,
        Platforms.CBS.value,
        Platforms.FOX.value,
        Platforms.THE_CW.value,
        Platforms.SHUDDER.value,
        Platforms.SYFY.value,
        Platforms.POPCORNFLIX.value,
        Platforms.VUDU.value,
        Platforms.FREEFORM.value,
        Platforms.PLUTO_TV.value,
        Platforms.TUBI_TV.value,
    ],
}

ALL_PLATFORMS = [service.value for service in Platforms]
ALL_PLATFORMS_MAP = {i: ix for ix, i in enumerate(ALL_PLATFORMS)}
