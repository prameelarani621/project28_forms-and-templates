from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
        return HttpResponse('insert_topic is done')
        
    return render(request,'insert_topic.html',d)



def insert_WebPage(request):
    EWFO=WebPageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebPageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
        return HttpResponse('insert_webpage is done')
        
    return render(request,'insert_WebPage.html',d)



def insert_AcessRecords(request):
    EAFO=AcessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AcessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
        return HttpResponse('insert_AccessRecord is done')
        
    return render(request,'insert_AcessRecords.html',d)