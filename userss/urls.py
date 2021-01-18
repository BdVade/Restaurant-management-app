from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

# Create your views here.

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('register/', views.register,name='register'),


]
