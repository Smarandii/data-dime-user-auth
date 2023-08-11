from django.urls import path

from . import views

urlpatterns = {
    path('', views.api_home),
    path('register/', views.api_home, name='register'),
    path('login/', views.api_home, name='login'),
    path('profile/', views.api_home, name='profile'),
}