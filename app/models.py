from django.db import models

# Create your models here.
class website(models.Model) :
    website_url=models.CharField(max_length=250)
    website_blocked=models.BooleanField(default='True')
    
    def __str__(self) :
        return self.website_url