from django.http import *
from django.shortcuts import render
from .dp import mood_detect
from recommendationapp.models import Song,Movie,Book
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render
global context
def index(request):
    global context
    
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    
def contact(request):
    return render(request,'contact.html')
def cssdemo(request):
    return render(request,"cssdemo.html")
def movies(request):
    global context
    context={}
    if "movobj" not in context:
        emotion=mood_detect()
        movobj1=Movie.objects.all()
        movobj=[]
        for i in movobj1:
            #if i.mood==context['emo']:
            if i.mood==emotion:
                movobj.append(i)
        #context["movobj"]=movobj
        context={"emo":emotion,"movobj":movobj}
    return render(request,"movies.html",context)
def books(request):
    global context
    context={}
    if "bokobj" not in context:
        emotion=mood_detect()
        bokobj1=Book.objects.all()
        bokobj=[]
        for i in bokobj1:
            #if i.mood==context['emo']:
            if i.mood==emotion:
                bokobj.append(i)
        #context["movobj"]=movobj
        context={"emo":emotion,"bokobj":bokobj}
    return render(request,"book.html",context)
def music(request):
    global context
    #if request.method=='POST':
    if True:
       emotion=mood_detect()
       songobj1=Song.objects.all()
       songobj=[]
       for i in songobj1:
           if i.mood==emotion:
               songobj.append(i)
       context={"emo":emotion,"songobj":songobj}
       #return render(request,"music.html",context)
    return render(request,"music.html",context)
def pdf(request):
    global context
    dict=request.POST
    bks=Book.objects.all()
    for i in bks:
        #print(i.name,dict)
        if i.name in dict:
            path1=i.book_file
            path1="C:/Users/praveenraj/Documents/emotion_based_recommendation_system_using_django/EMOTION_RECOMMENDATIO_SYS/media/"+str(path1)
            #print(path1,"hi")
            break
    #print(bks)
    #pdf1=open(r"C:\Users\praveenraj\Documents\emotion_based_recommendation_system_using_django\EMOTION_RECOMMENDATIO_SYS\media\media\books_dir\praveenresume.pdf","rb").read()
    pdf1=open(path1,"rb").read()
    return HttpResponse(pdf1,content_type="application/pdf")
