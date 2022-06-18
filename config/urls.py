from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from movies.api.urls import router as core_router

admin.site.site_header = "Strichka Admin"

api_router = routers.DefaultRouter()
api_router.registry.extend(core_router.registry)

handler403 = "movies.views.error_403"
handler404 = "movies.views.error_404"
handler500 = "movies.views.error_500"


urlpatterns = [
    path("", include("movies.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include(api_router.urls)),
    path("jet/", include("jet.urls", "jet")),
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        login_required(SpectacularSwaggerView.as_view(url_name="schema")),
        name="swagger-ui",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
