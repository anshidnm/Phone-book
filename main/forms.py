from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
    )

    mobile = forms.CharField(max_length=10,min_length=10,
    label="Mobile Number",
    required=True,
    widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Mobile'})
    )

class ContactEditForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control edit_name','placeholder':'Enter Your Name'}),
    )

    mobile = forms.CharField(max_length=10,min_length=10,
    label="Mobile Number",
    required=True,
    widget=forms.NumberInput(attrs={'class':'form-control edit_mobile','placeholder':'Enter Your Mobile'})
    )

    class Meta:
        model = Contact
        fields = "__all__"