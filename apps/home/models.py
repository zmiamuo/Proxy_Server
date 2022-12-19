

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

<<<<<<< HEAD
class website(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    website_url=models.URLField(max_length=250,null=False)
    website_blocked=models.BooleanField(default=True)
    
    def __str__(self):
        return self.website_url

=======


class Blocked(models.Model):
    blocked=models.CharField(max_length=255)

class DurationUsage(models.Model):
    duration=models.IntegerField(max_length=4)
    usage=models.IntegerField()
    ip_address=models.CharField(max_length=255)


class Availaible_ip(models.Model):
    Availaible_ip=models.CharField(max_length=255)
>>>>>>> refs/remotes/origin/main
