from typing import Any

from django.db import models

from common.cache import reset_endpoint_cache
from common.convert import slugify_value


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
        # Validate data
        if not self.is_cleaned:
            self.clean()

        # Clear cache
        reset_endpoint_cache(key_prefix=slugify_value(self._meta.verbose_name))  # type: ignore

        super().save(*args, **kwargs)

    def delete(self, *args: Any, **kwargs: Any) -> tuple[int, dict[str, int]]:
        # Clear cache
        reset_endpoint_cache(key_prefix=slugify_value(self._meta.verbose_name))  # type: ignore

        return super().delete(*args, **kwargs)
