from django import forms

class NameForm(forms.Form):
    clinet_name = forms.CharField(label='Client name', max_length=100)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=150)
    longitude = forms.DecimalField(max_digits=9, decimal_places=5, required=False)
    latitude = forms.DecimalField(max_digits=9, decimal_places=5, required=False)

