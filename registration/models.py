from django import forms
from django.core.validators import MinValueValidator
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class Registrant(models.Model):
    """
    Represents a person who will attend the annual session.
    """
    first_name = models.CharField(
        max_length=255
    )
    last_name = models.CharField(
        max_length=255
    )
    age = models.IntegerField(
        help_text="Age at time of the event.",
        validators=[
            MinValueValidator(0)
        ]
    )
    email = models.EmailField(
        help_text="Personal email for this registrant, if applicable.",
        null=True,
        blank=True,
    )
    attending_memorial_meeting_only = models.BooleanField(default=False)
    needs_ada_accessible_accommodations = models.BooleanField()
    days_attending = models.ManyToManyField(
        "event_days.EventDay", blank=True, default=True)
    overnight_accommodations = models.ForeignKey(
        "accommodations.Accommodation", on_delete=models.PROTECT, null=True, blank=True)
    registration_cost = models.FloatField(
        validators=[
            MinValueValidator(0)
        ]
    )

    def calculated_registration_cost(self):
        return "One million dollars!"

    panels = [
        FieldPanel("first_name"),
        FieldPanel("last_name"),
        FieldPanel("age"),
        FieldPanel("email"),
        FieldPanel("attending_memorial_meeting_only"),
        FieldPanel("needs_ada_accessible_accommodations"),
        FieldPanel("days_attending",
                   widget=forms.CheckboxSelectMultiple),
        FieldPanel("overnight_accommodations"),
    ]

    def full_name(self):
        return f"{ self.first_name } { self.last_name } (${ self.registration_cost })"

    def __str__(self):
        return self.full_name()


class RegistrationPage(Page):
    intro = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    max_count = 1
