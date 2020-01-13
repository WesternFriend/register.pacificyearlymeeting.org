from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from payments.models import Payment, RegistrantPayment


class PaymentModelAdmin(ModelAdmin):
    """Registrant model admin."""

    model = Payment
    menu_label = "Payments"
    menu_icon = "tick"
    menu_order = 110
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "amount",
    )


class RegistrantPaymentModelAdmin(ModelAdmin):
    """Registrant model admin."""

    model = RegistrantPayment
    menu_label = "Registrant Payments"
    menu_icon = "success"
    menu_order = 120
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = (
        "amount",
    )


modeladmin_register(PaymentModelAdmin)
modeladmin_register(RegistrantPaymentModelAdmin)
