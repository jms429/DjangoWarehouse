# Generated by Django 3.1 on 2020-08-30 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20200830_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='static/photos/default-photo.png', upload_to='static/photos/'),
        ),
    ]
