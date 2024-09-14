from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError

from catalog.models import Product, Version

class StyleFormMixin:
    """
    Mixin для стилизации формы.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
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


class VersionForm(StyleFormMixin, ModelForm):
    """Форма для создания и редактирования версии продукта"""

    class Meta:
        model = Version
        fields = ('version_number', 'version_name', 'version_active',)
