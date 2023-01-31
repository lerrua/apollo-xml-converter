from django import forms

class XMLConverterFileForm(forms.Form):
    file = forms.FileField(required=True)
