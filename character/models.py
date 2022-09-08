''' imports '''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Character(models.Model):
    ''' The Character Database '''
    name = models.CharField(max_length=200)
    character_class = models.CharField(max_length=200)
    background = models.TextField(null=True, blank=True)
    background_snippet = models.CharField(max_length=300, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="character_post")
    items = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.character_class} {self.name}"


class Equipment(models.Model):
    ''' The Character Equipment Database '''
    character = models.OneToOneField(Character, null=True, on_delete=models.CASCADE)
    head = models.CharField(max_length=300, null=True, blank=True)
    face = models.CharField(max_length=300, null=True, blank=True)
    shoulder_left = models.CharField(max_length=300, null=True, blank=True)
    shoulder_right = models.CharField(max_length=300, null=True, blank=True)
    torso = models.CharField(max_length=300, null=True, blank=True)
    back = models.CharField(max_length=300, null=True, blank=True)
    hand_left = models.CharField(max_length=300, null=True, blank=True)
    hand_right = models.CharField(max_length=300, null=True, blank=True)
    waist = models.CharField(max_length=300, null=True, blank=True)
    legs = models.CharField(max_length=300, null=True, blank=True)
    feet = models.CharField(max_length=300, null=True, blank=True)
    accessory_one = models.CharField(max_length=300, null=True, blank=True)
    accessory_two = models.CharField(max_length=300, null=True, blank=True)
    accessory_three = models.CharField(max_length=300, null=True, blank=True)
    accessory_four = models.CharField(max_length=300, null=True, blank=True)
    accessory_five = models.CharField(max_length=300, null=True, blank=True)
    accessory_six = models.CharField(max_length=300, null=True, blank=True)
    main_hand = models.CharField(max_length=300, null=True, blank=True)
    off_hand = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.character.name}'s Equipment"


class Note(models.Model):
    ''' The Note Database '''
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character_note')
    note = models.TextField()

    def __str__(self):
        return f"{self.note}"


class Picture(models.Model):
    ''' The Gallery Database '''
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character_pictures')
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"A picture of {self.character}"
