from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('update_profile/', UserEditView.as_view(), name='profile_edit'),
    path('password/', PasswordsChangeView.as_view(), name='password_change'),
    path('password_success', views.password_success, name='password_success'),
]
