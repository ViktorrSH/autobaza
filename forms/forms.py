from django import forms


class CarForm(forms.Form):
    name = forms.CharField(max_length=20)
    country = forms.CharField(max_length=20)

