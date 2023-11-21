from django import forms
from .models import UploadedImage

class ImageUploadForm(forms.ModelForm):
  class Meta:
    model = UploadedImage
    fields = ('image', 'prompt', 'num_samples', 'image_resolution', 'low_threshold', 'high_threshold', 'ddim_steps', 'scale', 'eta', 'a_prompt', 'n_prompt')