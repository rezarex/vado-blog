from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path("blogs/create_blog", views.create_blog, name="new-blog"),
    path("blogs/<id>", views.blog_detail, name="blog-detail"),
]