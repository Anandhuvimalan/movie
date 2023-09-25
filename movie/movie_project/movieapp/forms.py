from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'description', 'year', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control-file'
