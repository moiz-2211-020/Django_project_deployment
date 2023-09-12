from django.urls import path
from django.contrib import admin
from . import views

app_name= "matrimony"

urlpatterns = [
    
    path('', views.profileviews_list ,name= 'profile_view'),

    #this is the way of passing variable in urls
    path('<int:profile_id>', views.profile_details,name= 'profile_detail'),
    path("contact/", views.contact_us, name = "contact"),
    path("new_profile/", views.newprofileview, name = "new_profile"),
    path('delete_profile/', views.profile_delete_view, name = "profile_delete")
]