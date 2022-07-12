from django import forms
from django.core.exceptions import ValidationError
from mylib.validators import min_length_validators
from shipping.models import ShippingAddress


class SippingAddressForm(forms.ModelForm):
    zipcode = forms.CharField(validators=[min_length_validators])
    
    class Meta:
        model = ShippingAddress
        fields = ('city', 'zipcode', 'address', 'number')
        # exclude = ('user',)
        # fields = '__all__'
    
    # def clean_zipcode(self):
    #     zipcode = self.cleaned_data['zipcode']
    #     if len(zipcode) != 16:
    #         raise ValidationError("Length is not 16")
    #     return zipcode

    # def clean(self):
    #     cleaned_data = super().clean()
    #     return cleaned_data