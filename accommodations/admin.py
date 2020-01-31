from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from accommodations.models import Accommodation, AccommodationPrice


class AccommodationModelAdmin(ModelAdmin):
    """Registrant model admin."""

    model = Accommodation
    menu_label = "Accommodations"
    menu_icon = "fa-home"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "name",
    )


modeladmin_register(AccommodationModelAdmin)


class AccommodationPriceModelAdmin(ModelAdmin):
    """Registrant model admin."""

    model = AccommodationPrice
    menu_label = "Prices"
    menu_icon = "fa-usd"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "accommodation",
        "age_group",
        "price",
    )


modeladmin_register(AccommodationPriceModelAdmin)
