

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import website,DurationUsage,Availaible_ip
from django.shortcuts import redirect , render 
from django.contrib.auth.models import User



@login_required(login_url="/login/")
def index(request):
    
    objects=website.objects.filter(author=request.user)
    objects2=DurationUsage.objects.all()
    objects3=Availaible_ip.objects.all()
    
    if request.method=='POST' and  'add_websites' in request.POST:
        blocked_websites=request.POST.get('blocked')
        if str(blocked_websites) not in [ x.website_url for x in objects]:
             weburl= request.POST.get('blocked')
             data=website(author=request.user,website_url=weburl)
             data.save()
             return redirect(reverse(("home")))
    if request.method=='POST' and  'generate' in request.POST:
        duration=request.POST.get('Duration')
        usage=request.POST.get('Usage')
        ip_address=request.POST.get('ip_address')
        data2=DurationUsage(author=request.user,duration=duration,usage=usage,ip_address=ip_address)
        if duration and usage and ip_address:
            data2.save()
            return HttpResponseRedirect("/")




    context = {'segment': 'index',"blocked_websites":objects,"generated_proxy":objects2,"available_ips":objects3}
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
        id = request.user.id
        username = request.user.username  
        password = request.user.password
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        user=User(id=id,username=username,email=email, first_name=firstname,last_name=lastname,password=password)
        user.save(force_update=True)
        html_template = loader.get_template('home/user.html')
        return render(request,'home/user.html')