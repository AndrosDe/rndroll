''' imports '''
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django_summernote.widgets import SummernoteWidget

from event.models import Profile, GMPromotion, Messages


class SignUpForm(UserCreationForm):
    ''' The Form for the Register Site '''
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'placeholder': 'email@emailprovider.com'}))

    class Meta:
        '''Setting up the Input Formfields'''
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
            )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control border border-2 p-2 mb-2'
        self.fields['password1'].widget.attrs['class'] = 'form-control border border-2 p-2 mb-2'
        self.fields['password2'].widget.attrs['class'] = 'form-control border border-2 p-2 mb-2'


class EditUserSettingsForm(UserChangeForm):
    ''' The Form for the Settings Update Site '''
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2'}))

    class Meta:
        '''Setting up the Input Formfields'''
        model = User
        fields = ('username', 'email')


class PasswordsChangeForm(PasswordChangeForm):
    ''' The Form for the Password Change Site '''
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'type': 'password'}))

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfileForm(forms.ModelForm):
    ''' The Form for the Profile Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Profile
        fields = (
            'profile_pic',
            'bio',
            'website_url',
            'facebook_url',
            'twitter_url',
            'twitch_url',
            'instagram_url',
            'youtube_url',
            'pinterest_url',
            'discord_url'
            )

        widgets = {
            'bio': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px', 'title': 'Discripe yourself'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'type': 'file', 'accept': 'image/*', 'default': 'placeholder'}),
            'website_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.your.website.com'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.your.facebook-link.com'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.your.twitter-link.com'}),
            'twitch_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.your.twitch-channel.com'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.your.instagram-link.com'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.your.youtube-channel.com'}),
            'pinterest_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.your.pinterest-link.com'}),
            'discord_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.your.discord-invite.com'}),
        }


class GM_PromotionForm(forms.ModelForm):
    ''' The Form for the GM_Promotion Model '''

    class Meta:
        '''Setting up the Input Formfields for GM_Promotion'''
        model = GMPromotion
        fields = ('body',)

        widgets = {
            'body': forms.TextInput(
                attrs={'class': 'form-control', 'value': 'I would like to be a Game Master', 'id': 'body', 'type': 'hidden'}),
        }


class MessageForm(forms.ModelForm):
    ''' The Form for the User-Messages '''

    class Meta:
        '''Setting up the Input Formfields for User-Messages'''
        model = Messages
        fields = ('user', 'body')

        widgets = {
            'body': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px', 'title': 'Discripe yourself'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'owner', 'type': 'hidden'}),
        }
