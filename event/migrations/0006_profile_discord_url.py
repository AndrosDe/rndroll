# Generated by Django 3.2.15 on 2022-09-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_event_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='discord_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
