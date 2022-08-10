# Generated by Django 4.1 on 2022-08-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('CO', 'Contact'), ('AT', 'Attendant'), ('OR', 'Organisatior'), ('AD', 'Admin')], default='CO', max_length=2),
        ),
    ]