from django.urls import path
from . import views

urlpatterns = [
    path("u/<str:slugs>", views.urlRedirect, name="redirect"),
    path("error/d/<str:slugs>", views.disable, name="disable"),
    path("error/u/<str:slugs>", views.not_found, name="not_found")
]