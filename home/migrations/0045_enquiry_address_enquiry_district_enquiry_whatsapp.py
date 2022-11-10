# Generated by Django 4.1.1 on 2022-11-08 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_feedback_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='Address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enquiry',
            name='District',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enquiry',
            name='Whatsapp',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
