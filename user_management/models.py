from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # first_name = models.CharField(max_length=60, blank=True)
    # last_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=False)
    avatar = models.ImageField(upload_to='avatars', default="avatars/download.png", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    # def save(self, *args, **kwargs):
    #     # save the profile first
    #     super().save(*args, **kwargs)

        # img = Image.open(self.avatar.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     # create a thumbnail
        #     img.thumbnail(output_size)
        #     # overwrite the larger image
        #     img.save(self.avatar.path)

class GenerationDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_img = models.URLField()
    response_json = models.JSONField()
    output_img = models.URLField()
    generated_at = models.DateTimeField(auto_now_add=True)
