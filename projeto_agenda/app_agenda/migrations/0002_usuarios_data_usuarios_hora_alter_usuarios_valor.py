# Generated by Django 5.0.7 on 2024-08-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='data',
            field=models.DateField(default='2024-01-01'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='hora',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='valor',
            field=models.IntegerField(),
        ),
    ]
