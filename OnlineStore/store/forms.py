from django import forms
from .models import Item, ItemTag

class ProductSearchForm(forms.Form):
    search_term = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Поиск товаров...'}),
    )
    category = forms.ModelChoiceField(
        queryset=ItemTag.objects.all(),
        required=False,
    )