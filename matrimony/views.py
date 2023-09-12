from django.shortcuts import render,redirect
from .models import profile
from .form import Profileform,NewProfile
#for using formsets we import formset_factory
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required


def profileviews_list(request):
    profiles= profile.objects.all
    user = request.user
    return render(request,"matrimony/profile_view_list.html",{"profiles":profiles,'user':user})

def profile_details(request,profile_id):

    profil= profile.objects.get(id=profile_id)
    user = request.user
    return render(request,'matrimony/profile_detail.html',{"profile":profil,'user':user})

def profile_delete_view(request,profile_id):
    profile_id = profile.objects.get(id = profile_id)
    profile_id.delete()
    redirect( 'matrimony:profile_view')


def contact_us(request):
    
    if request.method== "POST":
        #we are storing the post request data in the vriable of form
        form = Profileform(request.POST)
        if form.is_valid():
            #the cleaned data is the django library that only works when variable pass the validation test
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"EMAIL: {form.cleaned_data['email']}")
            print(f"CONTACT NUMBER: {form.cleaned_data['contact_num']}")
            print(f"MESSAGE: {form.cleaned_data['message']}")
    else:
        form = Profileform

    return render(request,'matrimony/contact.html',{"form":form})

'''def newprofileview(request):
    
    if request.method == "POST":
        #we are storing the post request data in the vriable of form
        form = NewProfile(request.POST , request.FILES)
        if form.is_valid():
            #form.save function only works with modelforms 
            form.save()
            #when you want to redirect to any page so for that you need to specify the name of the page that you write in url file
            return redirect('matrimony:profile_view')
    else:
        form = NewProfile()

    return render(request,'matrimony/new_profile.html',{"form":form})'''


# Create your views here.


# use of Formsets
#we are using this login required decorator for the restriction in our website so user need to login first before filling the form
@login_required
def newprofileview(request):
    #here extra represent the number of forms in one page
    profile_formset = formset_factory(NewProfile , extra=1)
    
    if request.method == "POST":
        #we are storing the post request data in the vriable of form
        formset = profile_formset(request.POST , request.FILES)
        if formset.is_valid():
            #formset is actually works in list form like it save our form in list so we need to use for loop here for saving changes on multiple forms in one page
            for form in formset:
                if form.has_changed():
                    form.save()
            return redirect('matrimony:profile_view')


             
            
            #when you want to redirect to any page so for that you need to specify the name of the page that you write in url file
            #return redirect('matrimony:profile_view')
    else:
        formset = profile_formset
    
    user = request.user

    return render(request,'matrimony/new_profile.html',{"formset":formset,'user':user})


