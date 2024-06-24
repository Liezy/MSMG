from django import forms
from .models import Musica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'audio_link', 'letra_link', 'cifra_link', 'video_link']
