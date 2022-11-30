# Generated by Django 4.1.1 on 2022-11-28 09:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_about_album_banners_blog_contact_enquiry_feedback_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Mission_Title',
            field=models.CharField(blank=True, default='Mission', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='Vision_Title',
            field=models.CharField(blank=True, default='Vision', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='Description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='Mission',
            field=models.TextField(blank=True, null=True),
        ),
    ]
