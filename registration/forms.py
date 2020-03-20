from django import forms
from registration.models import Registrant
from registration.widgets import OvernightAccommodationsRadioSelect


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registrant
        exclude = ("user",)
