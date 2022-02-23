from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Url(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uri = models.CharField(max_length=10)
    url = models.URLField(max_length=1000)
    is_enable = models.BooleanField()
