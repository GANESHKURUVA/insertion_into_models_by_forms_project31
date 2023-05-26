from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse

def insert_topics(request):
    if request.method=='POST':
        topic=request.POST['gani']
        To=Topic.objects.get_or_create(topic_name=topic)[0]
        To.save()
        return HttpResponse(f'topic inserted{topic}')


    return render(request,'insert_topics.html')

def insert_webpage(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        topic=request.POST['to']
        name=request.POST['name']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=topic)

        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('success')
   
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    pass

    return render(request,'insert_access.html')