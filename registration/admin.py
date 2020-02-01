from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from registration.models import Registrant


class RegistrantModelAdmin(ModelAdmin):
    """Registrant model admin."""

    model = Registrant
    menu_label = "Registrants"
    menu_icon = "fa-address-book"
    menu_order = 201
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "full_name",
        "email",
        "needs_ada_accessible_accommodations",
        "calculated_registration_fee",
        "is_full_week_attender",
    )
    list_filter = (
        "overnight_accommodations",
        "needs_ada_accessible_accommodations",
        "attending_memorial_meeting_only",
        "days_attending",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )


modeladmin_register(RegistrantModelAdmin)
