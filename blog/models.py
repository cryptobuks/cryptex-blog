from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    post = RichTextField()

    display = models.BooleanField(default=True)

    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = 'Blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
