from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('view-blogs/<slug:blog_slug>/', views.blogViews, name='view_blog'),
    path('view-blogs/', views.blogViews, name='view_all_blogs'),
    path('', views.blogViews, name='home'),
]
