from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Blogsite(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField(null=True)
  img = models.ImageField(null=True,blank=True,upload_to='myapp')
  update_date = models.DateField(auto_now=True)
  publish_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)

  
  def __str__(self):
    return self.title

# settings.AUTH_USER_MODEL
