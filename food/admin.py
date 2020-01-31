from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from food.models import DietaryNeed, MealOption


class DietaryNeedModelAdmin(ModelAdmin):
    """Manage age groups."""

    model = DietaryNeed
    menu_label = "Dietary needs"
    menu_icon = "fa-cutlery"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "name",
    )


modeladmin_register(DietaryNeedModelAdmin)


class MealOptionModelAdmin(ModelAdmin):
    """Manage age groups."""

    model = MealOption
    menu_label = "Meal options"
    menu_icon = "fa-cutlery"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "name",
    )


modeladmin_register(MealOptionModelAdmin)
