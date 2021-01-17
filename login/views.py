from django.shortcuts import render, redirect

from .models import *

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def success(request):
    context = {
        "user": request.session['name'],
    }
    return render(request, 'success.html', context)

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()    
            new_user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            request.session['userid'] = new_user.id
            messages.success(request, "User successfully created")
            return redirect('/success')
    return redirect('/')

def user_login(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        login_errors = User.objects.login_validator(request.POST)
        login_email = request.POST['login_email']
        if len(login_errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user_list = User.objects.filter(email=login_email) 
            user = user_list[0]
            if user.password == request.POST['login_pass']:
                return redirect('/success')