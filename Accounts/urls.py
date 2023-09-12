from django.urls import path
from django.contrib import admin
from . import views

app_name= "Accounts"

urlpatterns = [
    
    path('register/', views.register ,name= 'register'),

    
    path('login/', views.login_view,name= 'login'),
    path('logout/', views.logout_view,name= 'logout'),
    path('delete/', views.delete_view,name= 'delete')

]