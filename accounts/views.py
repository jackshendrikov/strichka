from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from common.views import BaseView


class ProfileView(BaseView):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        return render(
            request=request,
            template_name="account/profile/profile.html",
            context=context,
        )
