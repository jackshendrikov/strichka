from django.db import models


class StrichkaBaseModel(models.Model):
    """
    Base model for all models in app.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
