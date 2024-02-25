from .models import Table
from django.forms import ModelForm, TextInput, Textarea

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ["title", "text", "prize"]
        widgets = {
            "title": TextInput(attrs={"class": "form_control", "placeholder": "Название товара"}),
            "text": Textarea(attrs={"class": "form_control", "placeholder": "Описание товара"}),
            "prize": TextInput(attrs={"class": "form_control", "placeholder": "Цена товара"}),
        }
