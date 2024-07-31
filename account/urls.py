from django.urls import path

from account import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('register/verify/', views.VerifyRegistration.as_view(), name='verify'),
    path('forgot/', views.ForgotPassword.as_view(), name='forgot'),
    path('forgot/verify/', views.VerifyForgotPassword.as_view(), name='forgot_verify'),
    path('forgot/verify/change/', views.SetNewPassword.as_view(), name='change_password'),
]

