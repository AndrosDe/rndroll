# Generated by Django 3.2.15 on 2022-09-18 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0008_alter_event_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game_master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_gm', to='event.profile'),
        ),
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(default='None', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='event_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]