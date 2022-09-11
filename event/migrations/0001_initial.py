# Generated by Django 3.2.15 on 2022-09-11 19:44

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('character', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('tag',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gm', models.BooleanField(default=False)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_pic', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, null=True, verbose_name='image')),
                ('website_url', models.CharField(blank=True, max_length=300, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=300, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=300, null=True)),
                ('twitch_url', models.CharField(blank=True, max_length=300, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=300, null=True)),
                ('youtube_url', models.CharField(blank=True, max_length=300, null=True)),
                ('pinterest_url', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GMPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('requested', models.BooleanField(default=False)),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gm_requests', to='event.profile')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('story', models.TextField()),
                ('snippet', models.CharField(max_length=300)),
                ('image', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('main_link', models.URLField(blank=True)),
                ('links', models.TextField(blank=True, null=True)),
                ('rule_set', models.CharField(blank=True, max_length=200, null=True)),
                ('shoutouts', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Private'), (1, 'Public'), (2, 'Expired')], default=0)),
                ('character_max', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=4)),
                ('characters', models.ManyToManyField(blank=True, related_name='event_characters', to='character.Character')),
                ('game_master', models.ForeignKey(blank=True, default='No Game Master', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='event_gm', to='event.profile')),
                ('likes', models.ManyToManyField(blank=True, related_name='event_like', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_creator', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(blank=True, related_name='event_tag', to='event.Tag')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='event.event')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
