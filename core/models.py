from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class UploadedImage(models.Model):
    image = models.FileField(upload_to='images/')
    prompt = models.CharField(max_length=200)
    N_SAMPLES = (('1', '1'), ('4', '4'))
    num_samples = models.CharField(max_length=1, choices=N_SAMPLES, default='1')
    IMAGE_RESOLUTION = (('256', '256x256'),
                        ('512', '512x512'),
                        ('768', '768x768'))
    image_resolution = models.CharField(max_length=10, choices=IMAGE_RESOLUTION, default=IMAGE_RESOLUTION[0][1])
    low_threshold = models.IntegerField(
        default=100, validators=[MinValueValidator(1),
                                 MaxValueValidator(255)])
    high_threshold = models.IntegerField(
        default=200, validators=[MinValueValidator(1),
                                 MaxValueValidator(255)])

    ddim_steps = models.IntegerField(default=20)
    scale = models.IntegerField(
        default=9, validators=[MinValueValidator(1),
                               MaxValueValidator(30)])
    eta = models.IntegerField(default=0)
    a_prompt = models.CharField(max_length=300, default="best quality, extremely detailed")
    n_prompt = models.CharField(max_length=300, default="longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality")

    def __str__(self):
        return self.image.name
