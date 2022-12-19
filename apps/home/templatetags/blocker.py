from django import template

register=template.Library()

@register.filter
def blocker(string) :
    import time
    from datetime import datetime as dt
    #Windows host file path
    hostsPath=r"C:/Windows/System32/drivers/etc/hosts"
    redirect="31.13.83.174"
    #Add the website you want to block, in this list
    websites=string
    while True:
        #Duration during which, website blocker will work
        if dt(dt.now().year,dt.now().month,dt.now().day,9) > dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
            print ("Sorry Not Allowed...")
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
            print ("Allowed access!")
        time.sleep(5)