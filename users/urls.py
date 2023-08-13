from django.urls import path

from . import views

urlpatterns = {
    path('', views.api_home),
    path('register/', views.api_register_user, name='register'),
    path('login/', views.api_login_user, name='login'),
    path('profile/', views.api_home, name='profile'),
}