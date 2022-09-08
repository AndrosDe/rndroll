''' imports '''
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

from .models import Character, Equipment, Note, Picture
from .forms import CharacterForm, EquipmentForm


class CharacterDetail(DetailView):
    ''' View for the Character Details '''
    model = Character
    template_name = "characters/character.html"


class CreateCharacter(CreateView):
    ''' Creating a Character '''
    model = Character
    form_class = CharacterForm
    template_name = "characters/character_create.html"


class EditCharacter(UpdateView):
    ''' Updateing a Character '''
    model = Character
    form_class = CharacterForm
    template_name = "characters/character_edit.html"
    success_url = reverse_lazy('home')


class DeleteCharacter(DeleteView):
    ''' Deleting an Character '''
    model = Character
    template_name = "characters/character_delete.html"
    success_url = reverse_lazy('home')


class CreateEquipment(CreateView):
    ''' Creating Equipment (for the first time) '''
    model = Equipment
    form_class = EquipmentForm
    template_name = "characters/equipment_create.html"


class EditEquipment(UpdateView):
    ''' Updateing Equipment '''
    model = Equipment
    form_class = EquipmentForm
    template_name = "characters/equipment_edit.html"
