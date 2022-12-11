from django import template
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.urls import reverse
from hashlib import md5

register = template.Library()

default_img_size = 300
default_selector = "_V1_SX{img_size}"
default_size_selector = default_selector.format(img_size=default_img_size)


@register.filter(name="gravatar")
def gravatar(user: User, size: int = 35) -> str:
    email = str(user.email.strip().lower()).encode("utf-8")
    email_hash = md5(email).hexdigest()
    url = "//www.gravatar.com/avatar/{0}?s={1}&d=identicon&r=PG"
    return url.format(email_hash, size)


@register.filter
def reduce_img_size(link: str, new_size: int) -> str:
    return link.replace(
        default_size_selector, default_selector.format(img_size=new_size)
    )


@register.simple_tag
def get_movie_url(is_movie: bool, movie_id: int) -> str:
    if is_movie:
        return reverse("movie_detail", kwargs={"pk": movie_id})
    return reverse("series_detail", kwargs={"pk": movie_id})


@register.simple_tag
def is_favorite(user: User, movie_id: int) -> bool:
    return user.profile.favorites.filter(pk=movie_id).exists()  # type: ignore


@register.simple_tag
def in_watchlist(user: User, movie_id: int) -> bool:
    return user.profile.watchlist.filter(pk=movie_id).exists()  # type: ignore


@register.simple_tag
def url_replace(request: HttpRequest, field: str, value: str) -> str:
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
