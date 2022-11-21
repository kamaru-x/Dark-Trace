# Generated by Django 4.1.1 on 2022-11-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_remove_enquiry_addedby_remove_feedback_addedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='about',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='album',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='album_image',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='album_image',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='album_image',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='banners',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='banners',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='banners',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contact',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='group_of_companies',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='group_of_companies',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='group_of_companies',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='manage_menu',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='manage_menu',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='manage_menu',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='quick_links',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quick_links',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='quick_links',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='EditedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='theme',
            name='EditedIp',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='Edited_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='about',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='album',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='album_image',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='album_image',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='banners',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='banners',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='group_of_companies',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group_of_companies',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='manage_menu',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='manage_menu',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='quick_links',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quick_links',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='AddedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='theme',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
    ]
