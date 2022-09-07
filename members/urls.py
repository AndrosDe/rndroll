''' imports '''
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, EditUserSettingsView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', EditUserSettingsView.as_view(), name='settings_edit'),
    path('password/', PasswordsChangeView.as_view(), name='password_change'),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile'),
    path('<int:pk>/update_profile_page', EditProfilePageView.as_view(), name='edit_profile'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile'),
]
