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
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
            request.session['name'] = request.POST['first_name']
            return redirect('/success')

def user_login(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
    
        return redirect('/success')