''' imports '''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User
from event.models import Profile, GMPromotion
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


class EditUserSettingsForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfileForm(forms.ModelForm):

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Profile
        fields = ('profile_pic', 'bio', 'website_url', 'facebook_url', 'twitter_url', 'twitch_url', 'instagram_url', 'youtube_url', 'pinterest_url')

        widgets = {
            'bio': SummernoteWidget(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'style': 'height: 280px', 'maxlength': '1000', 'placeholder': 'Discripe yourself within 1000 characters', 'title': 'Discripe yourself within 1000 characters'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'type': 'file', 'accept': 'image/*', 'default': 'placeholder'}),
            'website_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url'}),
            'twitch_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url'}),
            'pinterest_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url'}),
        }


class GM_PromotionForm(forms.ModelForm):
    ''' The Form for the GM_Promotion Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website GM_Promotion Application'''
        model = GMPromotion
        fields = ('body',)

        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control', 'value': 'I would like to be a Game Master',  'id': 'body', 'type': 'hidden'}),
        }
