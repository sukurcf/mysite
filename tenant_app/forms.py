from django import forms
from .models import Tenant
class TenantForm(forms.ModelForm):

    class Meta:
        model = Tenant
        fields = ('name', 'age', 'gender', 'mobile_1', 'mobile_2', 'mobile_3', 'address_1', 'city', 'country', 'location')