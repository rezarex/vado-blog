from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'is_active')
    search_fields = ('title', 'body', 'is_active')
    list_per_page = 10

admin.site.register(Blog, BlogAdmin)
