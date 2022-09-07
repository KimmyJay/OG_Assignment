from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage/', views.loginPage, name='loginpage'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registerpage/', views.registerPage, name='registerpage'),
    path('register/', views.registerUser, name='register'),
    
]
