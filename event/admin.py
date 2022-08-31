''' imports '''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.core.exceptions import ValidationError
from django import forms
from .models import Event, Tag, GameMaster


admin.site.register(Tag)


class EventForm(forms.ModelForm):
    ''' reviewing if characters to not exceet character_max '''
    model = Event

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('characters').count() < 1:
            print("No character seleceted")
        elif cleaned_data.get('characters').count() >= 1:
            if cleaned_data.get('characters').count() > (cleaned_data.get('character_max') + 2):
                raise ValidationError(f"You have to choose {(cleaned_data.get('character_max') + 2)} of characters for the Event!")


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    ''' Adminpanel Display of Creating an Event'''
    form = EventForm
    list_display = ('title', 'game_master', 'status', 'start_date')
    search_fields = ['title']
    list_filter = ('status', 'created_on', 'start_date')
    summernote_fields = ('story', 'excerpt', 'shoutouts')

    fieldsets = (

        (None, {'fields': ('title', 'image', 'tag', 'owner')}),
        (('Story & Excerpt'), {'fields': ('story', 'excerpt')}),
        (('Game Master & Players'), {'fields': ('game_master', 'character_max', 'characters')}),
        (('Start Date and links'), {'fields': ('start_date', 'main_link', 'links', 'shoutouts')}),
        (('Status'), {'fields': ('status',)}),
    )


admin.site.register(GameMaster)
