'''imports'''
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget
from .models import Event

class EventForm(forms.ModelForm):
    ''' The Form for the Event Model '''
    image = CloudinaryFileField()

    class Meta:
        ''' Setting up the Input Formfields for the Website Application '''
        model = Event
        fields = ('title', 'story', 'tag', 'image', 'game_master', 'main_link', 'links', 'rule_set', 'shoutouts', 'owner', 'start_date', 'status', 'character_max', 'characters')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'placeholder': 'A new adventure awaits'}),
            'story': SummernoteWidget(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'style': 'height: 250px', 'maxlength': '2000', 'placeholder': 'Discripe your event / setting within 2000 characters'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'type': 'file', 'accept': 'image/*', 'required': 'false'}),
            'game_master': forms.Select(attrs={'class': 'form-select'}),
            'main_link': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'www.the-link-where-one-can-whatch-this.com'}),
            'links': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 250px', 'maxlength': '500', 'placeholder': 'Put in other links, to your pateron or homepage or links to to the players channel, within 500 characters'}),
            'rule_set': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For example: DnD 5th Edition'}),
            'shoutouts': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 250px', 'maxlength': '1000', 'placeholder': 'Mention so addtional important stuff, like extra rules and thank people for their support within 100 characters'}),
            'owner': forms.Select(attrs={'class': 'form-select border border-2 border-warning p-2 mb-2'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'id': 'datetime-local', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-select border border-2 border-warning p-2 mb-2'}),
            'character_max': forms.Select(attrs={'class': 'form-select border border-2 border-warning p-2 mb-2'}),
            'characters': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
