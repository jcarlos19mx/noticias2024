from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
  edad = models.PositiveSmallIntegerField(null=True, blank=True)