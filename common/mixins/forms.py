from typing import TYPE_CHECKING

from django.contrib.admin import ModelAdmin
from django.db import models
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

if TYPE_CHECKING:
    _Base = ModelAdmin
else:
    _Base = object


class PreservePreviousFormInputsMixin(_Base):
    """
    Save previous fields inputs after submitting "save and add another" button.
    """

    preserve_inputs_fields: set[str]

    def _response_with_prev_form_values(
        self, request: HttpRequest, obj: type[models.Model]
    ) -> HttpResponse:
        prev_item_fields = request.POST.copy()

        prev_item_fields.pop("csrfmiddlewaretoken")
        prev_item_fields.pop("_addanother")

        url = reverse(
            f"admin:{obj._meta.app_label}_{obj._meta.model_name}_add"  # noqa: WPS437
        )
        qs = "&".join(
            f"{field}={value}"
            for field, value in prev_item_fields.items()
            if field in self.preserve_inputs_fields
        )
        url = f"{url}?{qs}"
        return HttpResponseRedirect(url)

    def response_change(
        self, request: HttpRequest, obj: type[models.Model]
    ) -> HttpResponse:
        if "_addanother" in request.POST:
            return self._response_with_prev_form_values(request, obj)

        return super().response_change(request, obj)

    def response_add(
        self,
        request: HttpRequest,
        obj: type[models.Model],
        post_url_continue: str | None = None,
    ) -> HttpResponse:
        if "_addanother" in request.POST:
            return self._response_with_prev_form_values(request, obj)

        return super().response_add(request, obj, post_url_continue)
