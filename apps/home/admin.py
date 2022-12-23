

from django.contrib import admin
from .models import website
from .models import DurationUsage
from .models import Availaible_ip


class Adminwebsite(admin.ModelAdmin):
    model = website
    list_display = ('id','author', 'website_url', 'website_blocked')


admin.site.register(website, Adminwebsite)

class AdminDurationUsage(admin.ModelAdmin):
    model = DurationUsage
    list_display = ('id','author', 'duration', 'usage','ip_address')

admin.site.register(DurationUsage,AdminDurationUsage)

class AdminAvailable_ip(admin.ModelAdmin):
    model = Availaible_ip
    list_display = ('id','Availaible_ip')
admin.site.register(Availaible_ip,AdminAvailable_ip)


