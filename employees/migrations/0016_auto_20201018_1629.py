# Generated by Django 3.1.2 on 2020-10-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0015_auto_20201018_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='machine_1',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='machine_2',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='machine_3',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='machine_4',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='machine_5',
        ),
        migrations.AlterField(
            model_name='department',
            name='level_1',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='department',
            name='level_2',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='department',
            name='level_3',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='department',
            name='level_4',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]
