from django.urls import path
from . import views

urlpatterns = [
    path("u/<str:slugs>", views.urlRedirect, name="redirect"),
    path("error/d/<str:slugs>", views.disable, name="disable")
]