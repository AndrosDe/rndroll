# Generated by Django 3.2.15 on 2022-09-10 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20220910_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gm_promotion',
            old_name='approved',
            new_name='requested',
        ),
    ]