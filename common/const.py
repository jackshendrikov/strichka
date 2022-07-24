from enum import Enum


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


ALL_PLATFORMS = [service.value for service in Platforms]
ALL_PLATFORMS_MAP = {i: ix for ix, i in enumerate(ALL_PLATFORMS)}
