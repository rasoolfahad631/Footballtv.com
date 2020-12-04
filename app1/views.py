from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from app1.models import Item
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView



# Create your views here.
def index(request):
    return render(request,"index.html")

def log(request):  
    if request.method == 'POST':                                                         
    	username=request.POST.get("username")
    	password=request.POST.get("password")
    	user = authenticate(username=username, password=password)
    	if user is not None:
    		login(request, user)
    		return redirect("videos")
    else:
        return render(request,"log.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save();
        return redirect("log")
    else:
        return render(request,"Register.html")

def videos(request):
    obj = Item.objects.all()
    return render(request,"Videos.html",{'obj': obj})

def add_video(request):
    if request.method == 'POST':
        u = Item()
        u.video =   request.POST.get('url')
        u.video_title = request.POST.get('title')
        u.save()
        return redirect('videos')

def play(request,id):
    m = get_object_or_404(Item,id=request.POST.get("video"))
    m.views = m.views + 1
    m.save()
    return render(request,"play.html",{'m': m})

# class ViewChart(TemplateView):
    # template_name = 'Analysis.html'
def analysis(request):
    context = Item.objects.all()
    return render(request,"Analysis.html",{'context': context})
    

def logouts(request):
    logout(request)
    return redirect("index")



        


