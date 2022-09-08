''' imports '''
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Character, Note, Picture
from .forms import CharacterForm, EquipmentForm, ItemForm


class CharacterDetail(DetailView):
    ''' View for the Character Details '''
    model = Character
    template_name = "characters/character.html"


class CreateCharacter(CreateView):
    ''' Creating a Character '''
    model = Character
    form_class = CharacterForm
    template_name = "characters/character_create.html"
    success_url = reverse_lazy('home')


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


class EditEquipment(UpdateView):
    ''' Updateing Equipment '''
    model = Character
    form_class = EquipmentForm
    template_name = "characters/equipment_edit.html"
    success_url = reverse_lazy('home')


class EditItem(UpdateView):
    ''' Updateing Equipment '''
    model = Character
    form_class = ItemForm
    template_name = "characters/item_edit.html"
    success_url = reverse_lazy('home')
