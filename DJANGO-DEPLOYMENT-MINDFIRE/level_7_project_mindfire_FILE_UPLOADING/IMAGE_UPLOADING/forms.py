from django import forms
from IMAGE_UPLOADING.models import ImageUploadModel

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=ImageUploadModel
        fields='__all__'
