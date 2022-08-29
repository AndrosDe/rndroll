''' imports '''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Character, Note, Picture


@admin.register(Character)
class CharacterAdmin(SummernoteModelAdmin):

    list_display = ('name', 'character_class', 'slug', 'created_by')
    prepopulated_fields = {'slug': ('name', 'character_class')}
    list_filter = ('name', 'created_by')
    summernote_fields = ('background')

    fieldsets = (
        (None, {'fields': ('character_class', 'name', 'slug', 'image', 'background')}),
        (('Equipment & Inventory'), {'fields': ('equipment', 'items',)}),
        (('User'), {'fields': ('created_by',)}),
    )


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):

    list_display = ('id', 'character')
    list_filter = ('character',)
    summernote_fields = ('note')


admin.site.register(Picture)
