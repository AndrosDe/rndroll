''' imports '''
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from event.models import Event
from .models import Character, Note
from .forms import CharacterForm, EquipmentForm, ItemForm, NoteForm


class CharacterDetail(DetailView):
    ''' View for the Character Details '''
    model = Character
    template_name = "characters/character.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CharacterDetail, self).get_context_data(*args, **kwargs)
        page_character = get_object_or_404(Character, id=self.kwargs['pk'])
        # adding the note form and notes to the page
        note_list = Note.objects.all
        note_form = NoteForm()

        # getting all the events that this character joined
        joined_events = Event.objects.filter(characters=page_character)

        context["note_form"] = note_form
        context["joined_events"] = joined_events
        context["note_list"] = note_list
        context["page_character"] = page_character
        return context

    def post(self, request, pk, *args, **kwargs):
        '''Getting the Note from the Page'''
        character = get_object_or_404(Character, id=self.kwargs['pk'])
        note_form = NoteForm(data=request.POST)

        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.character = character
            note.save()
        else:
            note_form = NoteForm()

        return HttpResponseRedirect(reverse("show_character", args=[str(pk)]))


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


class DeleteNote(DeleteView):
    ''' Deleting an Character '''
    model = Note
    template_name = "characters/note_delete.html"
    success_url = reverse_lazy('home')
