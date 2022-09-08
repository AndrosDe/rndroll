'''imports'''
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Character, Equipment


class CharacterForm(forms.ModelForm):
    ''' The Form for the Character Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Character
        fields = ('name', 'character_class', 'image', 'background', 'background_snippet', 'items', 'created_by')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2'}),
            'character_class': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'type': 'file', 'accept': 'image/*', 'default': 'placeholder'}),
            'background': SummernoteWidget(attrs={'class': 'form-control border border-2 p-2 mb-2', 'style': 'height: 280px', 'maxlength': '2000', 'placeholder': 'Discripe your event / setting within 2000 characters', 'title': 'Discripe your event / setting within 2000 characters'}),
            'background_snippet': forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'placeholder': 'Make a small story snippet of max.300 characters for your event.'}),
            'items': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px', 'maxlength': '500', 'placeholder': 'Put in other links, to your pateron or homepage or links to to the players channel, within 500 characters'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'value': '',  'id': 'owner', 'type': 'hidden'})
        }


class EquipmentForm(forms.ModelForm):
    ''' The Form for the Equipment Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Equipment
        fields = ('character', 'head', 'face', 'shoulder_left', 'shoulder_right', 'torso', 'back', 'hand_left', 'hand_right', 'waist', 'legs', 'feet', 'accessory_one', 'accessory_two', 'accessory_three', 'accessory_four', 'accessory_five', 'accessory_six', 'main_hand', 'off_hand')

        widgets = {
            'character': forms.Select(attrs={'class': 'form-select border border-2 border-warning p-2 mb-2'}),
            'head': forms.TextInput(attrs={'class': 'form-control'}),
            'face': forms.TextInput(attrs={'class': 'form-control'}),
            'shoulder_left': forms.TextInput(attrs={'class': 'form-control'}),
            'shoulder_right': forms.TextInput(attrs={'class': 'form-control'}),
            'torso': forms.TextInput(attrs={'class': 'form-control'}),
            'back': forms.TextInput(attrs={'class': 'form-control'}),
            'hand_left': forms.TextInput(attrs={'class': 'form-control'}),
            'hand_right': forms.TextInput(attrs={'class': 'form-control'}),
            'waist': forms.TextInput(attrs={'class': 'form-control'}),
            'legs': forms.TextInput(attrs={'class': 'form-control'}),
            'feet': forms.TextInput(attrs={'class': 'form-control'}),
            'accessory_one': forms.TextInput(attrs={'class': 'form-control'}),
            'accessory_two': forms.TextInput(attrs={'class': 'form-control'}),
            'accessory_three': forms.TextInput(attrs={'class': 'form-control'}),
            'accessory_four': forms.TextInput(attrs={'class': 'form-control'}),
            'accessory_five': forms.TextInput(attrs={'class': 'form-control'}),
            'accessory_six': forms.TextInput(attrs={'class': 'form-control'}),
            'main_hand': forms.TextInput(attrs={'class': 'form-control'}),
            'off_hand': forms.TextInput(attrs={'class': 'form-control'})
        }
