from django.urls import include, path

from accounts.views import ProfileView

urlpatterns = [
    path("", include("allauth.urls")),
    path("user/", ProfileView.as_view(), name="user_profile"),
    path("user/favorites", ProfileView.as_view(), name="user_favorites"),
    path("user/watchlist", ProfileView.as_view(), name="user_watchlist"),
    path("user/settings", ProfileView.as_view(), name="user_settings"),
]
