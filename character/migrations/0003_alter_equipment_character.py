# Generated by Django 3.2.15 on 2022-09-08 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_auto_20220908_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='character',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='character.character'),
        ),
    ]
