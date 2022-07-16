from typing import Any

from django.db.models import QuerySet
from django_filters.views import FilterView

from accounts.models import Profile
from movies.services.filters import MovieFilter


class BaseProfileView(FilterView):
    """Base User Watchlist & Favorites view."""

    page_title = ""
    filterset_class = MovieFilter
    paginate_by = 30
    template_name = "movies/movie_list.html"

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context[
            "page_title"
        ] = f"{self.page_title} ({self.get_queryset().count()} items)"
        return context


class WatchlistView(BaseProfileView):
    """User Watchlist view."""

    page_title = "My Watchlist"

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Profile.objects.get(user=user).watchlist


class FavoriteView(BaseProfileView):
    """User Favorite view."""

    page_title = "My Favorites"

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Profile.objects.get(user=user).favorites
