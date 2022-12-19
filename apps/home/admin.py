

from django.contrib import admin
from .models import website

# Register your models here.
<<<<<<< HEAD

class Adminwebsite(admin.ModelAdmin):
    model = website
    list_display = ('id','author', 'website_url', 'website_blocked')


admin.site.register(website, Adminwebsite)
=======
from .models import Blocked
from .models import DurationUsage
from .models import Availaible_ip


admin.site.register(Blocked)
admin.site.register(DurationUsage)
admin.site.register(Availaible_ip)

>>>>>>> refs/remotes/origin/main
