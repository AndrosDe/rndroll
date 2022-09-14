'''imports'''
from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Event, Comment


class EventForm(forms.ModelForm):
    ''' The Form for the Event Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Event
        fields = (
            'title',
            'story',
            'snippet',
            'tag',
            'image',
            'game_master',
            'main_link',
            'links',
            'rule_set',
            'shoutouts',
            'owner',
            'start_date',
            'status',
            'character_max',
            'characters'
            )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'placeholder': 'A new adventure awaits'}),
            'story': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px', 'title': 'Discripe your event / setting'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'title': 'Make a small story snippet of max.300 characters for your event.', 'value': 'Chick the event title above for more...'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'type': 'file', 'accept': 'image/*', 'default': 'placeholder'}),
            'game_master': forms.Select(attrs={'class': 'form-select'}),
            'main_link': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'https:\\\www.the-link-where-one-can-whatch-this.com', 'aria-label': 'Link To The Event'}),
            'links': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px'}),
            'rule_set': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For example: DnD 5th Edition'}),
            'shoutouts': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px'}),
            'owner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'owner', 'type': 'hidden'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'id': 'datetime-local', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-select border border-2 border-warning p-2 mb-2'}),
            'character_max': forms.Select(attrs={'class': 'form-select border border-2 border-warning p-2 mb-2'}),
            'characters': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }


class CommentForm(forms.ModelForm):
    ''' The Form for the Comment Model '''

    class Meta:
        '''Setting up the Input Formfields for Comment Application'''
        model = Comment
        fields = ('body',)

        widgets = {
            'body':  SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px'}),
        }
