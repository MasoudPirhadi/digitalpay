import uuid

from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

