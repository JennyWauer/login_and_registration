from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def register(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        return redirect('/success')