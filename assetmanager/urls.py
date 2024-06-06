from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("lists/", views.view_lists),
]
