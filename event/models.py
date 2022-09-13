''' imports '''
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from character.models import Character


STATUS = ((0, "Private"), (1, "Public"), (2, "Expired"))
MAX_PLAYER = ((2, 2), (3, 3), (4, 4), (5, 5), (6, 6))


class Tag(models.Model):
    ''' The Tag Database '''
    tag = models.CharField(
        max_length=200
    )

    class Meta:
        ''' ordering the Tag Database alphabetically '''
        ordering = ('tag',)

    def __str__(self):
        return f"{self.tag}"


class Profile(models.Model):
    ''' Extending the User Database with "Game Master"'''
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    gm = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)
    profile_pic = CloudinaryField(
        'image',
        null=True,
        blank=True,
        default='placeholder')
    website_url = models.CharField(max_length=300, null=True, blank=True)
    facebook_url = models.CharField(max_length=300, null=True, blank=True)
    twitter_url = models.CharField(max_length=300, null=True, blank=True)
    twitch_url = models.CharField(max_length=300, null=True, blank=True)
    instagram_url = models.CharField(max_length=300, null=True, blank=True)
    youtube_url = models.CharField(max_length=300, null=True, blank=True)
    pinterest_url = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        ''' in order to create an event on the Website '''
        return reverse('home')


class Event(models.Model):
    ''' The Event Database '''
    # main content
    title = models.CharField(max_length=200)
    story = models.TextField(null=True, blank=True)
    snippet = models.CharField(max_length=300)
    tag = models.ManyToManyField(
        Tag,
        related_name='event_tag',
        blank=True)
    image = CloudinaryField('image', default='placeholder', blank=True)
    # connecting to Player that will Game Master the Session
    game_master = models.ForeignKey(
        Profile,
        on_delete=models.SET_DEFAULT,
        default='No Game Master',
        related_name='event_gm',
        null=True,
        blank=True)
    # Fluff part of the Content
    main_link = models.URLField(max_length=200, blank=True)
    links = models.TextField(blank=True, null=True)
    rule_set = models.CharField(max_length=200, blank=True, null=True)
    shoutouts = models.TextField(blank=True, null=True)
    # Connecting to User
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='event_creator',
        null=True)
    # Dates
    start_date = models.DateTimeField(auto_now=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(
        choices=STATUS,
        default=0)
    # Player Section
    character_max = models.IntegerField(choices=MAX_PLAYER, default=4)
    characters = models.ManyToManyField(
        Character,
        related_name='event_characters',
        blank=True)
    # Likes
    likes = models.ManyToManyField(
        User,
        related_name='event_like',
        blank=True)

    class Meta:
        ''' ordering the events after start date '''
        ordering = ['start_date']

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        ''' in order to create an event on the Website '''
        return reverse('home')

    def number_of_likes(self):
        ''' counts the number of likes '''
        return self.likes.count()


class Comment(models.Model):
    ''' The Comment Database '''
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ''' ordering the comments after start date '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.event.title} - {self.name}"


class GMPromotion(models.Model):
    ''' The GM_Promotion Database '''
    profile = models.OneToOneField(
        Profile,
        null=True,
        on_delete=models.CASCADE,
        related_name="gm_requests")
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    requested = models.BooleanField(default=False)

    class Meta:
        ''' ordering the requests after start date '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.name} - {self.created_on}"


class Messages(models.Model):
    ''' The Comment Database '''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages",
        null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ''' ordering the comments after start date '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"Message from {self.user}"
