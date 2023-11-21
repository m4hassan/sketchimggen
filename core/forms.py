from django import forms
from .models import UploadedImage

class ImageUploadForm(forms.ModelForm):
  class Meta:
    model = UploadedImage
    fields = ('image', 'prompt', 'num_samples', 'image_resolution', 'low_threshold', 'high_threshold', 'ddim_steps', 'scale', 'eta', 'a_prompt', 'n_prompt')

class SdForm(forms.Form):
  init_img = forms.ImageField()
  prompt = forms.CharField(max_length=300)
  negative_prompt = forms.CharField(max_length=300)
  IMAGE_SIZE = (('256', '256x256'),
                ('512', '512x512'),
                ('768', '768x768'))
  image_size = forms.ChoiceField(choices=IMAGE_SIZE)
  samples = forms.CharField(max_length=1)
  num_inference_steps = forms.CharField(max_length=3)
  safety_checker = forms.CharField(max_length=3)
  enhance_prompt = forms.CharField(max_length=3)
  guidance_scale = forms.FloatField(max_value=40.0)
  strength = forms.FloatField(max_value=1.0)