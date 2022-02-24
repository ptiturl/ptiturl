from django.shortcuts import render, redirect

from .serializers import UrlSerializer

# Create your views here.

from .models import Url


def urlRedirect(request, slugs):
    try:
        data = Url.objects.get(uri=slugs)
    except Exception:
        return redirect(f"/error/u/{slugs}")
    else:
        if data.is_enable:
            return redirect(data.url)
        else:
            return redirect(f"/error/d/{slugs}")


def disable(request, slugs):
    return render(request, "disable.html", {"uri": slugs})


def not_found(request, slugs):
    return render(request, "not_found.html", {"uri": slugs})


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import Url
from .serializers import UrlSerializer
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly


class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True)
    def redirect(self, request, *args, **kwargs):
        url = self.get_object()
        return redirect(url.url)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)