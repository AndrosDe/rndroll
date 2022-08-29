''' imports '''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Character(models.Model):
    ''' The Character Database '''
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    character_class = models.CharField(max_length=200)
    background = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="character_post")
    items = models.TextField(blank=True)
    equipment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.character_class} {self.name}"


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
