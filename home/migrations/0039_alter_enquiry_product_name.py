# Generated by Django 4.1.1 on 2022-11-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_remove_enquiry_time_alter_enquiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='Product_Name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
