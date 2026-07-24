from django import forms
from .models import Address


class AddressForm(forms.ModelForm):

    class Meta:

        model = Address

        fields = [
            "full_address",
            "landmark",
            "pincode",
            "mobile",
        ]

        widgets = {

            "full_address": forms.Textarea(attrs={
                "class":"form-control",
                "rows":4
            }),

            "landmark": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "pincode": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "mobile": forms.TextInput(attrs={
                "class":"form-control"
            }),

        }