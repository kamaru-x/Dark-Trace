# Generated by Django 4.1.1 on 2022-11-08 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_alter_product_options_alter_service_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Website',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
