''' imports '''
from django.urls import path
from .views import CharacterDetail, CreateCharacter, EditCharacter, DeleteCharacter


urlpatterns = [
    path('<int:pk>/character', CharacterDetail.as_view(), name='show_character'),
    path('create_character/', CreateCharacter.as_view(), name='character_create'),
    path('character/edit/<int:pk>', EditCharacter.as_view(), name='character_edit'),
    path('character/<int:pk>/remove', DeleteCharacter.as_view(), name='character_delete'),
]
