# Generated by Django 3.1 on 2020-08-30 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default='static/img/default-photo.png', upload_to='static/photos/'),
        ),
    ]