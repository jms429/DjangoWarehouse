# Generated by Django 3.1.2 on 2020-10-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_auto_20201013_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='color_hex',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AddField(
            model_name='department',
            name='icon_url',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]