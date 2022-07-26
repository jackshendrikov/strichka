from typing import Any

from django.contrib import admin
from django.db.models import QuerySet


class StrichkaBaseModelAdmin(admin.ModelAdmin):
    list_display = ("created_at", "updated_at")

    def delete_queryset(self, request: Any, queryset: QuerySet) -> None:
        for obj in queryset:
            obj.delete()
