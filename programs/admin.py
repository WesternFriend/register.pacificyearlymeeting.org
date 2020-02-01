from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from programs.models import ProgramChoice


class ProgramChoiceModelAdmin(ModelAdmin):
    """Manage program choices."""

    model = ProgramChoice
    menu_label = "Program choices"
    menu_icon = "fa-users"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "name",
        "age_min",
        "age_max",
    )
    list_filter = ("age_min", "age_max")


modeladmin_register(ProgramChoiceModelAdmin)
