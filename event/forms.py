'''imports'''
from django import forms
from django_summernote.widgets import SummernoteWidget

from character.models import Character
from .models import Event, Comment


class EventForm(forms.ModelForm):
    ''' The Form for the Event Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Event
        fields = ('title', 'story', 'snippet', 'tag', 'image', 'game_master', 'main_link', 'links', 'rule_set', 'shoutouts', 'owner', 'start_date', 'status', 'character_max', 'characters')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'placeholder': 'A new adventure awaits'}),
            'story': SummernoteWidget(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'style': 'height: 280px', 'maxlength': '2000', 'placeholder': 'Discripe your event / setting within 2000 characters', 'title': 'Discripe your event / setting within 2000 characters'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'placeholder': 'Make a small story snippet of max.300 characters for your event.'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'type': 'file', 'accept': 'image/*', 'default': 'placeholder'}),
            'game_master': forms.Select(attrs={'class': 'form-select'}),
            'main_link': forms.URLInput(attrs={'class': 'form-control', 'id': 'url', 'type': 'url', 'placeholder': 'www.the-link-where-one-can-whatch-this.com'}),
            'links': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px', 'maxlength': '500', 'placeholder': 'Put in other links, to your pateron or homepage or links to to the players channel, within 500 characters'}),
            'rule_set': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For example: DnD 5th Edition'}),
            'shoutouts': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px', 'maxlength': '1000', 'placeholder': 'Mention so addtional important stuff, like extra rules and thank people for their support within 100 characters'}),
            'owner': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'value': '',  'id': 'owner', 'type': 'hidden'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'id': 'datetime-local', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-select border border-2 border-warning p-2 mb-2'}),
            'character_max': forms.Select(attrs={'class': 'form-select border border-2 border-warning p-2 mb-2'}),
            'characters': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }


class JoinForm(forms.ModelForm):
    ''' The Form for the JoinEvent Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Join Event Application'''
        model = Event
        fields = ('characters',)

        widgets = {
            'characters': forms.RadioSelect(attrs={'class': 'list-group-numbered list-group-horizontal','id': 'character_list'})
        }

    def __init__(self, user, *args, **kwargs):
        super(JoinForm, self).__init__(*args, **kwargs)
        self.fields['characters'].queryset = Character.objects.filter(created_by=user)


class CommentForm(forms.ModelForm):
    ''' The Form for the Comment Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Comment Application'''
        model = Comment
        fields = ('body',)

        widgets = {
            'body':  SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px'}),
        }
