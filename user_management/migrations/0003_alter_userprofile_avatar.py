# Generated by Django 4.2.7 on 2023-12-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_userprofile_first_name_userprofile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='download.png', null=True, upload_to='avatars'),
        ),
    ]
