# Generated by Django 4.1.1 on 2022-11-18 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0049_theme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theme',
            old_name='primary',
            new_name='Primary',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='secondary',
            new_name='Secondary',
        ),
    ]
