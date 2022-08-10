# Generated by Django 3.2.12 on 2022-08-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_lecture_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='available_timeslots',
            field=models.CharField(default='', max_length=2048),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='available_timeslots',
            field=models.CharField(max_length=2048),
        ),
    ]
