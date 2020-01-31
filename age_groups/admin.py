from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from age_groups.models import AgeGroup


class AgeGroupModelAdmin(ModelAdmin):
    """Registrant model admin."""

    model = AgeGroup
    menu_label = "Age groups"
    menu_icon = "fa-users"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "name",
    )


modeladmin_register(AgeGroupModelAdmin)
