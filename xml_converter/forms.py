from django import forms
from django.core.validators import FileExtensionValidator


class XMLConverterFileForm(forms.Form):
    file = forms.FileField(required=True, validators=[FileExtensionValidator(["xml"])])
