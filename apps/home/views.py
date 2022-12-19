# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import website
from django.shortcuts import redirect , render 
from django.contrib.auth.models import User


@login_required(login_url="/login/")
def index(request):
    if request.method =='POST' :
        weburl=request.POST.get('blocked','empty')
        new_website=website(author=request.user,website_url=weburl)
        new_website.save()
        return redirect(reverse('home'))
    else :
        urls = website.objects.filter(author=request.user)
        context = {'segment': 'index' , 'weburls':urls}

        html_template = loader.get_template('home/index.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

    
@login_required(login_url="/login/")
def updateuser(request):
    if request.method =='POST' :
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        update_user=User(first_name=firstname,last_name=lastname,email=email)
        update_user.save()
        return redirect(reverse('updateuser'))