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
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "full_name",
        "age",
        "email",
        "needs_ada_accessible_accommodations",
        "is_full_week_attender",
        "total_partial_day_discount",
        "registration_fee",
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
