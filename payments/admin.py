from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from payments.models import Payment


class PaymentModelAdmin(ModelAdmin):
    """Manage payments."""

    model = Payment
    menu_label = "Payments"
    menu_icon = "fa-money"
    menu_order = 102
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "paid_by",
        "amount",
    )


modeladmin_register(PaymentModelAdmin)
