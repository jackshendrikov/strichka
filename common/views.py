from typing import Any

import logging
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponseBase
from django.views.generic.base import View

JSON_DUMPS_PARAMS = {"ensure_ascii": False}
logger = logging.getLogger(__name__)


def is_ajax(request: HttpRequest) -> bool:
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


class BaseView(View):
    """
    Base class for all views, handles exceptions.
    """

    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseBase:
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.warning(e)
            return self._response({"errorMessage": str(e)}, status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        return response

    @staticmethod
    def _response(data: Any, *, status: int = 200) -> JsonResponse:
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
            json_dumps_params=JSON_DUMPS_PARAMS,
        )
