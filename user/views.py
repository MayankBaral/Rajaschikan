from django.shortcuts import redirect, render
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegister,UserUpdate,ShippingUpdate
from .models import UserProfile,User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from homepage.urls import *
# Create your views here.
@csrf_protect
def signup(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = UserRegister()

    template = loader.get_template('user/signup.html')
    return render(request,'user/signup.html',{'form':form})

def sign(request):
    template = loader.get_template('user/sign.html')
    return render(request,'user/sign.html')

@csrf_protect
@login_required
def profile(request):
    user_profile = UserProfile.objects.get(users=request.user)
    
    if request.method == "POST":
        p_form = UserUpdate(request.POST,instance=request.user)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('profile')
    else:
        p_form = UserUpdate(instance=request.user)

    if request.method == "POST":
        su_form = ShippingUpdate(request.POST,instance=request.user.userprofile)
        if su_form.is_valid():
            su_form.save()
            return redirect('profile')
    else:
        su_form = ShippingUpdate(instance=request.user.userprofile)

    context = {'user_profile':user_profile,'p_form':p_form,'su_form':su_form}

    template = loader.get_template('user/profile.html')
    return render(request,'user/profile.html',context)