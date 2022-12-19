

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class website(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    website_url=models.URLField(max_length=250,null=False)
    website_blocked=models.BooleanField(default=True)
    
    def __str__(self):
        return self.website_url

