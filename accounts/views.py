from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method== 'POST':
        messages.error(request,'test errors')
        return redirect('register')
    else:    
        return render(request,'accounts/register.html')
def login(request):
    if request.method== 'POST':
        pass
    else:    
        return render(request,'accounts/login.html')
def logout(request):
    return render('index')
def dashboard(request):
    return render(request,'accounts/dashbourd.html')
