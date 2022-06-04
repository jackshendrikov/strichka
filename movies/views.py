from typing import Any

from django.http import JsonResponse
from django.views.generic import View
from rest_framework.request import Request


class TestView(View):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> JsonResponse:
        return JsonResponse({}, status=204)
