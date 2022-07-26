from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from django.http import HttpRequest


class UserSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def signup(self, request: HttpRequest, user: User) -> User:
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user
