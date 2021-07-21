from django import forms
from .models import PhotoDiary

class PhotoDiaryForm(forms.ModelForm):
    class Meta:
        model = PhotoDiary
        fields = ['image', 'body']