from django import forms
from .models import Crowd

class CrowdForm(forms.ModelForm):
    class Meta:
        model = Crowd
        fields = ['image_name', 'scene_img']