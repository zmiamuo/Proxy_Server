# from urllib import request
# from django import template
# from django.shortcuts import redirect
# from django.contrib.auth.models import User
# from sys import platform
# import requests
# import os
# from ..models import DurationUsage
# import subprocess
# liste_blocked=[x.ip_address for x in DurationUsage.objects.filter(author=request.user)]
# if platform=="win32":

#     register=template.Library()

#     @register.filter
#     def blocker(string) :
#         import time
#         from datetime import datetime as dt
#         #Windows host file path
#         hostsPath=r"C:/Windows/System32/drivers/etc/hosts"
#         redirect="127.0.0.1"
#         #Add the website you want to block, in this list
#         websites=string
#     #Duration during which, website blocker will work is from 9 am to 6 pm
#         if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
#             print ("...")
#             with open(hostsPath,'r+') as file:
#                 content = file.read()
#                 if websites in content:
#                     pass
#                 else:
#                     file.write(redirect+" "+websites+"\n")
#         else:
#             with open(hostsPath,'r+') as file:
#                 content = file.readlines()
#                 file.seek(0)
#                 for line in content:
#                     if not websites in line :
#                         file.write(line)
#                 file.truncate()
#             print ("!!!")
# elif platform == "linux" or platform == "linux2":
#     if len(liste_blocked)!=0:
#         for i in liste_blocked:
#             build_str='echo 127.0.01'+' '+str(i)+'>> /etc/hosts'
#             os.system(build_str)
# elif platform == "darwin":

#     def block_website(website):
#         with open("/etc/hosts", "a") as f:
#             for i in :
#                 f.write(f"127.0.0.1 {i}\n")
#         subprocess.run(["dscacheutil", "-flushcache"])

# def unblock_website(website):
#     with open("/etc/hosts", "r") as f:
#         lines = f.readlines()
#     with open("/etc/hosts", "w") as f:
#         for line in lines:
#             if website not in line:
#                 f.write(line)
#     subprocess.run(["dscacheutil", "-flushcache"])


        




    