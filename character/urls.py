''' imports '''
from django.urls import path
from .views import CharacterDetail, CreateCharacter, EditCharacter, DeleteCharacter, EditEquipment, EditItem


urlpatterns = [
    path('<int:pk>/character', CharacterDetail.as_view(), name='show_character'),
    path('create_character/', CreateCharacter.as_view(), name='character_create'),
    path('character/edit/<int:pk>', EditCharacter.as_view(), name='character_edit'),
    path('character/<int:pk>/remove', DeleteCharacter.as_view(), name='character_delete'),
    path('equipment/edit/<int:pk>', EditEquipment.as_view(), name='equipment_edit'),
    path('item/edit/<int:pk>', EditItem.as_view(), name='item_edit'),
]
