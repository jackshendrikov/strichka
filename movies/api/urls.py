from rest_framework import routers

from movies.api.views import (
    CastViewSet,
    CategoryViewSet,
    CollectionViewSet,
    CountryViewSet,
    MovieViewSet,
    StreamingPlatformViewSet,
)

app_prefix = "core"

router = routers.SimpleRouter()
router.register(f"{app_prefix}/cast", CastViewSet, basename="api_cast")
router.register(f"{app_prefix}/category", CategoryViewSet, basename="api_category")
router.register(f"{app_prefix}/country", CountryViewSet, basename="api_country")
router.register(f"{app_prefix}/movies", MovieViewSet, basename="api_movies")
router.register(
    f"{app_prefix}/platforms", StreamingPlatformViewSet, basename="api_stream_platforms"
)
router.register(
    f"{app_prefix}/collections", CollectionViewSet, basename="api_collection"
)
