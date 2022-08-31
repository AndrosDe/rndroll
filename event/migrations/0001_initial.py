# Generated by Django 3.2.15 on 2022-08-29 16:43

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GameMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gm', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('story', models.TextField()),
                ('excerpt', models.TextField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('main_link', models.URLField(blank=True)),
                ('links', models.TextField(blank=True, null=True)),
                ('rule_set', models.CharField(blank=True, max_length=200, null=True)),
                ('shoutouts', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Private'), (1, 'Public'), (2, 'Expired')], default=0)),
                ('character_max', models.IntegerField(choices=[(0, '2'), (1, '3'), (2, '4'), (3, '5'), (4, '6')], default=2)),
                ('characters', models.ManyToManyField(blank=True, related_name='event_characters', to='character.Character')),
                ('game_master', models.ForeignKey(blank=True, default='No Game Master', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='event_gm', to='event.gamemaster')),
                ('likes', models.ManyToManyField(blank=True, related_name='event_like', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(default='Unknown User', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='event_creator', to=settings.AUTH_USER_MODEL)),
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
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='event.event')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
