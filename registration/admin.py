from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from registration.models import Registrant


class RegistrantModelAdmin(ModelAdmin):
    """Registrant model admin."""

    model = Registrant
    menu_label = "Registrants"
    menu_icon = "group"
    menu_order = 101
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "full_name",
        "registration_cost"
    )
    search_fields = (
        "first_name",
        "last_name",
    )


modeladmin_register(RegistrantModelAdmin)
