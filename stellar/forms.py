from django import forms
from stellar.models import Stellar
class StellarForm(forms.ModelForm):
    class Meta:
        model = Stellar
        fields = "__all__"