from django import forms
from store.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address',
                  'city',
                  'state',
                  'zipcode']

        widgets = {
                'address': forms.TextInput(attrs={
                    'placeholder': 'Address...',
                    'class': 'form-control'
                }),
                'city': forms.TextInput(attrs={
                    'placeholder': 'City...',
                    'class': 'form-control'
                }),
                'state': forms.TextInput(attrs={
                    'placeholder': 'State...',
                    'class': 'form-control'
                }),
                'zipcode': forms.TextInput(attrs={
                    'placeholder': 'Zipcode...',
                    'class': 'form-control'
                }),
            }
