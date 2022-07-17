from typing import Any

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from movies.models import Movie


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(
        Movie, verbose_name="Favorite movies", blank=True, related_name="user_favorites"
    )
    watchlist = models.ManyToManyField(
        Movie,
        verbose_name="Watchlist movies",
        blank=True,
        related_name="user_watchlist",
    )

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


@receiver(post_save, sender=User)
def create_user_profile(
    sender: type[User], instance: User, created: bool = False, **kwargs: Any
) -> None:
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender: type[User], instance: User, **kwargs: Any) -> None:
    instance.profile.save()  # type: ignore
