from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import profile, profile_pic, WalletBalance
from investapp.models import Silver,  Gold, Bronzs


# Create your views here.

def index(request):
    username = profile.objects.all()
    return render(request,'TordiPages/index.html', {'username': username})

def logout(request):
    auth.logout(request)
    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
     else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        birthday_date = request.POST['birthday_date']
        location = request.POST['location']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('TordiLogin/register')
    else:
        return render(request, 'TordiLogin/register.html')


def reset_password(request):
    return render(request, 'TordiLogin/reset_password.html')


def set_password(request):
    return render(request, 'TordiLogin/set_password.html')


@login_required
def invest(request):
    silver = Silver.objects.all()
    bronzs = Bronzs.objects.all()
    gold = Gold.objects.all()
    return render(request, 'TordiPages/invest.html', {'silver': silver}, {'gold': gold}, {'bronzs': bronzs})

@login_required
def wallet(request):
    wallet = WalletBalance.objects.all()
    return render(request, 'TordiPages/wallet.html', {'wallet': wallet})

@login_required
def edit_profile(request):
    return render(request, 'profiles/edit_profile.html')

@login_required
def view_profile(request):
    return render(request, 'profiles/view_profile.html')

@login_required
def how(request):
    return render(request, 'TordiPages/how.html')

@login_required
def about(request):
    return render(request, 'TordiPages/about.html')


@login_required
def view_profile(request):
    profile = profile.objects.all
    return render(request, 'profiles/view_profile.html', {'profile': profile})


# Change Password
def dashboard(request):
    return render(request, 'registration/dashboard.html')

def base(request):
    return render(request, 'base.html')