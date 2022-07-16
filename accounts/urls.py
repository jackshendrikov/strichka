from django.contrib.auth.decorators import login_required
from django.urls import include, path

from accounts.views import FavoriteView, WatchlistView

urlpatterns = [
    path("", include("allauth.urls")),
    path(
        "user/favorites", login_required(FavoriteView.as_view()), name="user_favorites"
    ),
    path(
        "user/watchlist", login_required(WatchlistView.as_view()), name="user_watchlist"
    ),
]
