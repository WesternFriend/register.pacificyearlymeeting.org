from django import forms
from registration.models import Registrant


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registrant
        exclude = ()
        widgets = {
            "days_attending": forms.CheckboxSelectMultiple()
        }
