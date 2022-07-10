from django import forms
from shipping.models import ShippingAddress


class SippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ('city', 'zipcode', 'address', 'number')
        # exclude = ('user',)
        # fields = '__all__'
    
    
