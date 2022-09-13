''' imports '''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Character(models.Model):
    ''' The Character Database '''
    name = models.CharField(max_length=200)
    character_class = models.CharField(max_length=200)
    background = models.TextField(null=True, blank=True)
    background_snippet = models.CharField(
        max_length=300, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="character_post"
    )
    items = models.TextField(null=True, blank=True)
    equipt_head = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_face = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_shoulder_left = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_shoulder_right = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_torso = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_back = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_hand_left = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_hand_right = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_waist = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_legs = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_feet = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_accessory_one = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_accessory_two = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_accessory_three = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_accessory_four = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_accessory_five = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_accessory_six = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_main_hand = models.CharField(
        max_length=300, null=True, blank=True)
    equipt_off_hand = models.CharField(
        max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.character_class} {self.name}"


class Note(models.Model):
    ''' The Note Database '''
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='character_note'
    )
    note = models.TextField()

    def __str__(self):
        return f"{self.note}"
