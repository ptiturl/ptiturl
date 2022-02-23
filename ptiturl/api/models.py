from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

class Url(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uri = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=1000)
    is_enable = models.BooleanField()
