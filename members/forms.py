from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'placeholder': 'email@emailprovider.com'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
 
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control border border-2 border-warning p-2 mb-2'
        self.fields['password1'].widget.attrs['class'] = 'form-control border border-2 border-warning p-2 mb-2'
        self.fields['password2'].widget.attrs['class'] = 'form-control border border-2 border-warning p-2 mb-2'
