# Generated by Django 5.1.1 on 2024-09-04 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='username',
            new_name='name',
        ),
    ]
