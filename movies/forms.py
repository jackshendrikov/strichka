from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from movies.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", "user")


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password"]
