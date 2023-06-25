from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .utils import *
from django.contrib.auth.decorators import login_required



# Create your views here.


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

@login_required(login_url='/login/') 
def booking(request):
    return render(request,'booking.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')


def register(req):
    if req.method == 'POST':
        first_name = req.POST.get('first_name')
        last_name = req.POST.get('last_name')
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(req, 'Username already taken')
            return redirect('/register/')
        
        send_email_to_user(username,email)        
        user = User.objects.create(first_name = first_name, last_name = last_name,  username = username, email = email, is_active = False)
        user.set_password(password)
        user.save()
        
        messages.info(req, 'Email Sent, Please verify your email address')
        
        return redirect("/register/")

    return render(req, 'register.html')

    # return render(request,'register.html')



def login_page(req):

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(req, 'Invalid username')
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(req, 'Invalid password')
            return redirect('/login/')       
        else:
            login(req, user)
            return redirect('/booking/')

    return render(req, 'login.html')



    # return render(request,'login.html')



def logout_page(req):
    logout(req)
    return redirect('/')

def profile(request):
    return render(request,'profile.html')

def update_profile(request):
    return render(request,'update_profile.html')

def edit_booking(request):
    return render(request,'edit_booking.html')

def additional(request):
    return render(request,'additional.html')

def extra(request):
    return render(request,'extra.html')
