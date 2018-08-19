from django.shortcuts import render

from .models import *


def blogViews(request, blog_slug=None):
    if blog_slug:
        blog = Blog.objects.get(slug=blog_slug)

        return render(request, 'blog/blog-detail.html', dict(blog=blog))

    else:
        if '/' in request.path:
            blogs = Blog.objects.all().order_by('-created')[:25]

            return render(request, 'blog/blog-list.html', dict(blogs=blogs))
        elif '/view-blogs/' in request.path:
            blogs = Blog.objects.all().order_by('-created')

            return render(request, 'blog/blog-list.html', dict(blogs=blogs))
