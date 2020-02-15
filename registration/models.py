from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

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
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="registrants",
    )

    def is_full_week_attender(self):
        total_event_days = EventDay.objects.count()

        number_of_days_attending = self.days_attending.count()

        if number_of_days_attending == total_event_days:
            return True

        return False

    def total_partial_day_discount(self):
        partial_day_discounts = [
            day.partial_day_discount for day in self.days_attending.all()]

        return sum(partial_day_discounts)

    def registration_fee(self):
        days_attending = self.days_attending.all()

        number_of_days_attending = len(days_attending)

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

            # full week attenders have specific fee
            if self.is_full_week_attender():
                return relevant_accommodation_fee.full_week_fee

            # daily attenders have day rate multiplied by days attending
            # they also qualify for daily discount based on partial days
            total_partial_day_discount = self.total_partial_day_discount()

            return relevant_accommodation_fee.daily_fee * number_of_days_attending - total_partial_day_discount

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
        FieldPanel("user"),
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

    def get_context(self, request, *args, **kwargs):
        # Avoid circular dependency
        from registration.forms import RegistrationForm

        context = super().get_context(request)

        context["registration_form"] = RegistrationForm

        return context

    def serve(self, request, *args, **kwargs):
        # Avoid circular dependency
        from registration.forms import RegistrationForm

        if request.method == "POST":
            registration_form = RegistrationForm(request.POST)

            if registration_form.is_valid():
                registration = registration_form.save()

                # Associate user with registration
                registration.user = request.user
                registration.save()

                messages.success(request, 'Registration added successfully!')

                return redirect("/")
        else:
            return super().serve(request)


class MyRegistrantsPage(Page):
    intro = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)

        context["my_registrants"] = request.user.registrants.all()

        return context


class EditRegistrantPage(Page):
    intro = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        registrant_id = request.GET["registrant_id"]

        if registrant_id:
            # Avoid circular dependency
            from registration.forms import RegistrationForm

            registrant = get_object_or_404(Registrant, pk=registrant_id)

            # prepopulate model form with registrant (dictionary)
            registrant_form = RegistrationForm(
                initial=model_to_dict(registrant))

            context["registrant_form"] = registrant_form

        return context

    def serve(self, request, *args, **kwargs):
        registrant_id = request.GET["registrant_id"]

        if registrant_id:
            registrant = get_object_or_404(Registrant, pk=registrant_id)

            # Make sure request user is authorized to edit registrant
            if request.user.id is not registrant.user.id:
                # TODO: make this error page a bit more user friendly
                # e.g. by rendering it in the base.html
                return HttpResponse('Unauthorized', status=401)

        return super().serve(request)
