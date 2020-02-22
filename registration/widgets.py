from django.forms.widgets import RadioSelect

from fees.models import AccommodationFee


class OvernightAccommodationsRadioSelect(RadioSelect):
    # Attach attributes from accommodation fee to each accommodation fee option
    # - age min
    # - age max
    # - full week fee
    # - daily fee
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super(OvernightAccommodationsRadioSelect, self).create_option(
            name, value, label, selected, index, subindex=None, attrs=None)

        accommodation_fee_pk = option["index"]

        try:
            accommodation_fee = AccommodationFee.objects.get(pk=1)
        except:
            print("No accommodation fee found with given primary key.")
            accommodation_fee = None

        if accommodation_fee is not None:
            option["attrs"]["data-age-min"] = accommodation_fee.age_min
            option["attrs"]["data-age-max"] = accommodation_fee.age_max
            option["attrs"]["data-full-week-fee"] = accommodation_fee.full_week_fee
            option["attrs"]["data-daily-fee"] = accommodation_fee.daily_fee

        return option
