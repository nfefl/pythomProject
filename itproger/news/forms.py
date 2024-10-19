from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['tittle', 'anons', 'full_text', 'date', 'make']

        widgets = {
            "tittle": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Полный текст',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
            }),
            "make": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип',
            }),

        }
