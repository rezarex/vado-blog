from django.db import models
from django.contrib import admin
from .models import Blog
from markdownx.widgets import AdminMarkdownxWidget
#from martor.widgets import AdminMartorWidget



class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    list_display = ('title', 'is_active')
    search_fields = ('title', 'is_active')
    list_per_page = 10

admin.site.register(Blog, BlogAdmin)
