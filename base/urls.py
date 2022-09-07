from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage/', views.loginPage, name='login_page'),
    path('registerpage/', views.registerPage, name='register_page'),
    path('artistapplypage/', views.artistApplyPage, name='artist_apply_page'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('artistapply/', views.artistApply, name='artist_apply'),

]
