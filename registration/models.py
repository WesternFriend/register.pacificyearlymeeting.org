from django import forms
from django.core.validators import MinValueValidator
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from fees.models import AccommodationFee, DayAttenderFee
from event_days.models import EventDay


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

    def is_full_week_attender(self):
        total_event_days = EventDay.objects.count()

        number_of_days_attending = self.days_attending.count()

        if number_of_days_attending == total_event_days:
            return True

        return False

    def calculated_registration_fee(self):
        number_of_days_attending = self.days_attending.count()

        if self.attending_memorial_meeting_only:
            # Memorial-only attendees are free
            return 0
        if self.overnight_accommodations:
            # Use Accommodation Fee structure
            relevant_accommodation_fee = AccommodationFee.objects.get(
                age_min__lte=self.age,
                age_max__gte=self.age,
                accommodation=self.overnight_accommodations,
            )

            if self.is_full_week_attender():
                return relevant_accommodation_fee.full_week_fee

            return relevant_accommodation_fee.daily_fee * number_of_days_attending

        # Default to day attender fee
        relevant_day_attender_fee = DayAttenderFee.objects.get(
            age_min__lte=self.age,
            age_max__gte=self.age
        )

        return relevant_day_attender_fee.daily_fee * number_of_days_attending

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
        return f"{ self.first_name } { self.last_name }"

    def __str__(self):
        return self.full_name()


class RegistrationPage(Page):
    intro = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    max_count = 1
