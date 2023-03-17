from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path("create_blog", views.create_blog, name="new-blog"),
]