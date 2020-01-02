from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
def register(request):
    if request.method== 'POST':
        # messages.error(request,'test errors')
        # return redirect('register')
        # get form data
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        #check if  password match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'that username is taken')
                return redirect('register') 
            else:
                if User.objects.filter(email=email).exists():
                  messages.error(request,'that email is taken')
                  return redirect('register') 
                else:
                    #looks good
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    # auth.login(request,user)
                    # messages.success(request,'you login succsess') 
                    # return redirect('index') 

                    user.save()
                    messages.success(request,'you login succsess')
                    return redirect('login')

        else:
            messages.error(request,'password not match')    

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
