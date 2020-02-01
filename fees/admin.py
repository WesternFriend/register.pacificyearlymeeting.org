from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from fees.models import DayAttenderFee, AccommodationFee


class DayAttenderFeeModelAdmin(ModelAdmin):
    """Manage day attender fees."""

    model = DayAttenderFee
    menu_label = "Day attender fees"
    menu_icon = "fa-usd"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "age_min",
        "age_max",
        "daily_fee",
    )
    ordering = (
        "age_min",
        "age_max",
    )


class AccommodationFeeModelAdmin(ModelAdmin):
    """Accommodation price model admin."""

    model = AccommodationFee
    menu_label = "Accommodation fees"
    menu_icon = "fa-usd"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "age_min",
        "age_max",
        "accommodation",
        "daily_fee",
        "full_week_fee"
    )
    list_filter = (
        "accommodation",
    )


class FeesModelAdminGroup(ModelAdminGroup):
    menu_label = "Fee structure"
    menu_icon = "fa-usd"
    menu_order = 192
    items = (
        DayAttenderFeeModelAdmin,
        AccommodationFeeModelAdmin,
    )


modeladmin_register(FeesModelAdminGroup)
