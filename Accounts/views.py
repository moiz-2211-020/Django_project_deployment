from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from .form import Registrationform
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def register(request):
    if request.method== 'POST':
       
        form=Registrationform(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect('Accounts:login')
    else:
        form = Registrationform()

    return render(request,'Accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            
            user = form.get_user()
            login(request, user)
            return redirect('matrimony:profile_view')
            
    else:
        form = UserCreationForm()

    return render(request,'Accounts/login.html',{"form":form})


def logout_view(request):
    logout(request)
    if request.method == "POST":
        return JsonResponse({'success':True})
    return redirect('Accounts:login')
    
    

def delete_view(request):
    request.user.delete()
    messages.success(request, "Your account is deleted successfully")
    return redirect("Accounts:login")
    

    
    