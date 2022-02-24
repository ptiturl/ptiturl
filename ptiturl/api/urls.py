from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'url', views.UrlViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path("auth/createuser", views.UserCreateAPIView.as_view()),
    path("u/<str:slugs>", views.urlRedirect, name="redirect"),
    path("error/d/<str:slugs>", views.disable, name="disable"),
    path("error/u/<str:slugs>", views.not_found, name="not_found")
]