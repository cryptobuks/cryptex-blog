from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'display', ]
    list_editable = ['display', ]
    search_fields = ['author', 'title', ]
    prepopulated_fields = {'slug': ('author', 'title', ), }
    list_per_page = 10


admin.site.register(Blog, BlogAdmin)
