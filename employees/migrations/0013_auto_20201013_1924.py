# Generated by Django 3.1.2 on 2020-10-13 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_auto_20201013_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]