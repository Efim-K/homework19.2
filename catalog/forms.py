from django.forms import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class ProductForm(ModelForm):
    """Форма для создания и редактирования продукта"""

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        """ Проверка на запрещенные слова в имени продукта  """
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        name = self.cleaned_data['name']
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError(f'Имя продукта не должно содержать запрещенное слово: {word}')
        return name

    def clean_depiction(self):
        """ Проверка на запрещенные слова в описании продукта  """
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        depiction = self.cleaned_data['depiction']
        for word in forbidden_words:
            if word in depiction.lower():
                raise ValidationError(f'Описание продукта не должно содержать запрещенное слово: {word}')
        return depiction


class VersionForm(ModelForm):
    """Форма для создания и редактирования версии продукта"""

    class Meta:
        model = Version
        fields = ('version_number', 'version_name', 'version_active',)
