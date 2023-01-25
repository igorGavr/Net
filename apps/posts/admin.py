from django.contrib import admin

# Register your models here
from apps.posts.models import Post

admin.site.register(Post)