from django import forms
from .models import CarApplication

class CarApplicationForm(forms.ModelForm):
    class Meta:
        model = CarApplication
        fields = ['car_brand', 'car_model', 'car_year', 'engine_volume', 'car_photo', 'description']
        widgets = {
            'car_year': forms.NumberInput(attrs={
                'min': 1900, 
                'max': 2025,
                'placeholder': 'Например: 2020'
            }),
            'engine_volume': forms.NumberInput(attrs={
                'step': '0.1',
                'min': '0.5',
                'max': '10.0',
                'placeholder': 'Например: 2.0'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Описание автомобиля...'
            }),
        }
    
    def clean_car_year(self):
        year = self.cleaned_data['car_year']
        if year < 1900 or year > 2025:
            raise forms.ValidationError("Год выпуска должен быть между 1900 и 2025")
        return year
    
    def clean_engine_volume(self):
        volume = self.cleaned_data['engine_volume']
        if volume <= 0 or volume > 10:
            raise forms.ValidationError("Объем двигателя должен быть от 0.5 до 10.0 литров")
        return volume