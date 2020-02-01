from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from fees.models import DayAttenderFee, AccommodationPrice


class DayAttenderFeeModelAdmin(ModelAdmin):
    """Manage day attender fees."""

    model = DayAttenderFee
    menu_label = "Day attender prices"
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


class AccommodationPriceModelAdmin(ModelAdmin):
    """Accommodation price model admin."""

    model = AccommodationPrice
    menu_label = "Prices"
    menu_icon = "fa-usd"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "accommodation",
        "price",
    )
    list_filter = (
        "accommodation",
    )


modeladmin_register(AccommodationPriceModelAdmin)
