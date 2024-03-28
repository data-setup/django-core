# profiles/urls.py
from django.urls import path
from . import views

app_name = 'profiles'  # Add app namespace

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]

