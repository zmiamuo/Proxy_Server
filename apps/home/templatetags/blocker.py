from django import template
from django.shortcuts import redirect
from django.contrib.auth.models import User


register=template.Library()

@register.filter
def blocker(string) :
    import time
    from datetime import datetime as dt
    #Windows host file path
    hostsPath=r"C:/Windows/System32/drivers/etc/hosts"
    redirect="127.0.0.1"
    #Add the website you want to block, in this list
    websites=string
    #Duration during which, website blocker will work is from 9 am to 6 pm
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print ("...")
        with open(hostsPath,'r+') as file:
            content = file.read()
            if websites in content:
                pass
            else:
                file.write(redirect+" "+websites+"\n")
    else:
        with open(hostsPath,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not websites in line :
                    file.write(line)
            file.truncate()
        print ("!!!")


    