from typing import Any

from django.db import models


class StrichkaBaseModel(models.Model):
    """
    Base model for all models in app.
    """

    is_cleaned = False

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> None:
        if not self.is_cleaned:
            self.clean()

        super().save(*args, **kwargs)
