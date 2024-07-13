from django.db import models
from django.contrib.auth.models import AbstractUser


#Abstract user 
class User(AbstractUser):
  """
  Custom User model with additional fields
  """
  #following = models.ManyToManyField('self', symmetrical=False, related_name='followers', null=True)

