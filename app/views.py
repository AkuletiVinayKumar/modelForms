from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TFO = TopicForm()
    d = {'TFO':TFO}
    if request.method == 'POST':
        TFOD = TopicForm(request.POST)
        if TFOD.is_valid:
            TFOD.save()

            return HttpResponse("Topic data is subitted successfully ")
    return render (request,'insert_topic.html',d)

def insert_webpage(request):
    WFO = WebpageForm()
    d = {'WFO': WFO }
    if request.method == 'POST':
        WFOD = WebpageForm(request.POST)
        if WFOD.is_valid:
            WFOD.save()
            return HttpResponse("Webpage data is submitted successfully")

    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    ARFO = AccessRecordForm()
    d = {'ARFO':ARFO }
    if request.method == 'POST':
        ARFOD = AccessRecordForm(request.POST)
        if ARFOD.is_valid:
            ARFOD.save()
            return HttpResponse("Access Reord data is inserted successfully")



    return render(request,'insert_accessrecord.html',d)