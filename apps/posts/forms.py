from django import forms

from apps.posts.models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "image",
            "description",
        ]
        widgets = {
            "image": forms.FileInput(
                attrs = {"class":"form-control"},
            ),
            "description": forms.Textarea(
                attrs= {"class":"form-control"}
            )
        }
        labels = {
            "image": "Изображение",
            "description": "Описание публикации"
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "description",
            "image",
        ]
        widgets = {
            "image": forms.FileInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs= {"class":"form-control"}
            )
        }
        labels = {
            "description": "Описание публикации"
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"class":"form-control"}
            )
        }
        labels = {
            "content": "Коментар"
        }
