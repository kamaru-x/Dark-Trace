# Generated by Django 4.1.4 on 2022-12-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_appbnr'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='ApiDate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='ApiTime',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
