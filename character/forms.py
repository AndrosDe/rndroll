'''imports'''
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Character, Note, Picture


class CharacterForm(forms.ModelForm):
    ''' The Form for the Character Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Character
        fields = (
            'name',
            'character_class',
            'image',
            'background',
            'background_snippet',
            'items',
            'created_by'
            )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2'}),
            'character_class': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'file', 'type': 'file', 'accept': 'image/*', 'default': 'placeholder'}),
            'background': SummernoteWidget(attrs={'class': 'form-control border border-2 p-2 mb-2', 'style': 'height: 280px', 'maxlength': '2000', 'title': 'Discripe your event / setting within 2000 characters'}),
            'background_snippet': forms.TextInput(attrs={'class': 'form-control border border-2 p-2 mb-2', 'placeholder': 'Make a small story snippet of max.300 characters.'}),
            'items': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control border border-2 border-warning p-2 mb-2', 'value': '', 'id': 'owner', 'type': 'hidden'})
        }


class EquipmentForm(forms.ModelForm):
    ''' The Form for the Equipment Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Character
        fields = (
            'equipt_head',
            'equipt_face',
            'equipt_shoulder_left',
            'equipt_shoulder_right',
            'equipt_torso',
            'equipt_back',
            'equipt_hand_left',
            'equipt_hand_right',
            'equipt_waist',
            'equipt_legs',
            'equipt_feet',
            'equipt_accessory_one',
            'equipt_accessory_two',
            'equipt_accessory_three',
            'equipt_accessory_four',
            'equipt_accessory_five',
            'equipt_accessory_six',
            'equipt_main_hand',
            'equipt_off_hand'
            )

        widgets = {
            'equipt_head': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_face': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_shoulder_left': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_shoulder_right': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_torso': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_back': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_hand_left': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_hand_right': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_waist': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_legs': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_feet': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_accessory_one': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_accessory_two': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_accessory_three': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_accessory_four': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_accessory_five': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_accessory_six': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_main_hand': forms.TextInput(attrs={'class': 'form-control'}),
            'equipt_off_hand': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ItemForm(forms.ModelForm):
    ''' The Form for the Item Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Character
        fields = ('items',)

        widgets = {
            'items': SummernoteWidget(attrs={'class': 'form-control', 'style': 'height: 280px'})
        }


class NoteForm(forms.ModelForm):
    ''' The Form for the Notes Model '''
    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Note
        fields = ('note',)

        labels = {'note': '', }

        widgets = {
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PictureForm(forms.ModelForm):
    ''' The Form for the Picture Model '''

    class Meta:
        '''Setting up the Input Formfields for the Website Application'''
        model = Picture
        fields = ('image',)

        widgets = {
            'image': SummernoteWidget(attrs={'class': 'form-control'}),
        }
