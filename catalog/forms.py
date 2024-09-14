from django.forms import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        name = self.cleaned_data['name']
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError(f'Имя продукта не должно содержать запрещенное слово: {word}')
        return name

    def clean_depiction(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        depiction = self.cleaned_data['depiction']
        for word in forbidden_words:
            if word in depiction.lower():
                raise ValidationError(f'Описание продукта не должно содержать запрещенное слово: {word}')
        return depiction
