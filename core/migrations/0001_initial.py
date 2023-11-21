# Generated by Django 4.2.7 on 2023-11-20 12:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/')),
                ('prompt', models.CharField(max_length=200)),
                ('num_samples', models.CharField(choices=[('1', '1'), ('4', '4')], default='1', max_length=1)),
                ('image_resolution', models.CharField(choices=[('256', '256x256'), ('512', '512x512'), ('768', '768x768')], default='256x256', max_length=10)),
                ('low_threshold', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(255)])),
                ('high_threshold', models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(255)])),
                ('ddim_steps', models.IntegerField(default=20)),
                ('scale', models.IntegerField(default=9, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)])),
                ('eta', models.IntegerField(default=0)),
                ('a_prompt', models.CharField(default='best quality, extremely detailed', max_length=300)),
                ('n_prompt', models.CharField(default='longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality', max_length=300)),
            ],
        ),
    ]