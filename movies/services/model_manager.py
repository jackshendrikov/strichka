from django.db import models
from django.db.models.aggregates import Count, Sum
from random import randint


class VoteManager(models.Manager):
    use_for_related_fields = True

    def likes(self) -> models.QuerySet:
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self) -> models.QuerySet:
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self) -> int:
        return self.vote.aggregate(Sum("vote")).get("vote__sum") or 0  # type: ignore


class MovieManager(models.Manager):
    def get_random_movie(self) -> models.QuerySet:
        count = self.aggregate(count=Count("id"))["count"]
        random_index = randint(0, count - 1)  # noqa: S311
        return self.all()[random_index]  # type: ignore
