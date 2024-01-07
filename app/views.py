from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)

    return render(request,'insert_topic.html')

def webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['n']
        u=request.POST['u']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
        WO.save()

        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)
    
    return render(request,'insert_webpage.html',d)

def accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        n=request.POST['n']
        d=request.POST['d']
        a=request.POST['a']
        WO=Webpage.objects.get(name=n)
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
        AO.save()
    
        QLAO=AccessRecord.objects.all()
        d1={'accessrecords':QLAO}
        return render(request,'display_accessrecord.html',d1)

    return render(request,'insert_accessrecord.html',d)


def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics': QLTO}
    if request.method =='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple_webpage.html',d)