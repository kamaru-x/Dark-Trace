# Generated by Django 4.1.4 on 2022-12-30 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0068_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='Currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.currency'),
        ),
    ]
