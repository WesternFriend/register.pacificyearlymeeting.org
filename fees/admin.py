from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from fees.models import DayAttenderFee, AccommodationFee


class DayAttenderFeeModelAdmin(ModelAdmin):
    """Manage day attender fees."""

    model = DayAttenderFee
    menu_label = "Day attender fees"
    menu_icon = "fa-money"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "age_min",
        "age_max",
        "daily_fee",
    )


modeladmin_register(DayAttenderFeeModelAdmin)


class AccommodationFeeModelAdmin(ModelAdmin):
    """Accommodation price model admin."""

    model = AccommodationFee
    menu_label = "Accommodation fees"
    menu_icon = "fa-usd"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "accommodation",
        "fee",
    )
    list_filter = (
        "accommodation",
    )


modeladmin_register(AccommodationFeeModelAdmin)
