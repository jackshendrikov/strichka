from django import forms

from movies.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", "user")
