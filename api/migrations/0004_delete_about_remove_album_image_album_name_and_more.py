# Generated by Django 4.1.1 on 2022-11-30 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_about_mission_title_about_vision_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.RemoveField(
            model_name='album_image',
            name='Album_Name',
        ),
        migrations.DeleteModel(
            name='Banners',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Group_Of_Companies',
        ),
        migrations.DeleteModel(
            name='Manage_Menu',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Quick_Links',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Album_Image',
        ),
    ]
