from django.shortcuts import render, redirect
from django.contrib import messages
# pyrefly: ignore [missing-import]
from .models import Contact, Momo
import re

from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    buf = Momo.objects.filter(category='buf')
    veg = Momo.objects.filter(category='veg')
    chicken = Momo.objects.filter(category='chicken')

    return render(request, 'app1/index.html', {'buf': buf, 'veg': veg, 'chicken': chicken})

def about(request):
    return render(request, 'app1/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'app1/contact.html')

def menu(request):
    return render(request, 'app1/menu.html')

def services(request):
    return render(request, 'app1/services.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                if AuthUser.objects.filter(username = username).exists():
                    messages.error(request, 'username already exists!')
                    return redirect('register')

                if AuthUser.objects.filter(email = email).exists():
                    messages.error(request, 'email already used!')
                    return redirect('register')

                if not email.endswith('@gmail.com'):
                    messages.error(request, 'please enter a valid gmail address')
                    return redirect('register')
                # if len(password) < 8:
                #     messages.error(request, 'password must be atleast of 8 character!')
                #     return redirect('register')
                # elif not re.search(r'[A-Z]', password):
                #     messages.error(request, 'enter atleast one upper case letter')
                #     return redirect('register')
                # elif not re.search(r'[0-9]', password):
                #     messages.error(request, 'enter atleast one integer')
                #     return redirect('register')
                # special character
                # atleast euta lowercase

                validate_password(password)

                AuthUser.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                messages.success(request, 'account created successfully')
                return redirect('index')

            except ValidationError as e:
                for error in e.messages:
                    messages.error(request, error)
                return redirect('register')
            
    return render(request, 'auth/register.html')

def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        if not AuthUser.objects.filter(username = username).exists():
            messages.error(request, 'username not found ')
            return redirect('log_in')
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(10000)
                else:
                    request.session.set_expiry(0)

                messages.success(request, 'login successful')
                return redirect('index')
            else:
                messages.error(request, 'Incorrect password!')
                return redirect('log_in')
    

    return render(request, 'auth/login.html')

def log_out(request):
    logout(request)
    return redirect('log_in')

@login_required(login_url='log_in')
def change_password(request):
    form = PasswordChangeForm(user=request.user)


    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'password changed')
            return redirect('log_in')


    return render(request, 'auth/change_password.html', {'form': form})

def user_profile(request):
    return render(request, 'auth/user_profile.html')