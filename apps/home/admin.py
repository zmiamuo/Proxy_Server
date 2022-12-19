

from django.contrib import admin
from .models import website
from .models import DurationUsage
from .models import Availaible_ip


class Adminwebsite(admin.ModelAdmin):
    model = website
    list_display = ('id','author', 'website_url', 'website_blocked')


admin.site.register(website, Adminwebsite)


admin.site.register(DurationUsage)
admin.site.register(Availaible_ip)


