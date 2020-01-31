from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from event_days.models import EventDay


class EventDayModelAdmin(ModelAdmin):
    """Registrant model admin."""

    model = EventDay
    menu_label = "Event days"
    menu_icon = "fa-calendar"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "date",
        "partial_day_discount",
    )


modeladmin_register(EventDayModelAdmin)
