from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'placeholder': 'email@emailprovider.com'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control border border-2 p-2 mb-2'
        self.fields['password1'].widget.attrs['class'] = 'form-control border border-2 p-2 mb-2'
        self.fields['password2'].widget.attrs['class'] = 'form-control border border-2 p-2 mb-2'


class UserEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))
    last_login = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'disabled': 'True'}))
    is_superuser = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check border border-2 p-2 mb-2', 'disabled': 'True'}))
    is_staff = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check border border-2 p-2 mb-2', 'disabled': 'True'}))
    is_active = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class': 'form-check border border-2 p-2 mb-2', 'disabled': 'True'}))
    date_joined = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'disabled': 'True'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active')


class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))
    new_password1 = forms.CharField(label= "New Password", widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))
    new_password2 = forms.CharField(label= "Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
