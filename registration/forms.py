from django import forms
from registration.models import Registrant


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registrant
        exclude = (None,)
        widgets = {
            "days_attending": forms.CheckboxSelectMultiple()
        }
