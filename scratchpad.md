Table schema

- lower age limit
- upper age limit
- full week (True or False)
- day
- overnight (True or False)
- accommodation
- fee


Here are some initial observations, and an attempt to separate threads of pricing into discrete parts.

    Memorial meeting only is free, so no food or accommodations need to be calculated.
    Day attenders aren't charged for accommodations, nor are they shown accommodation options. Day rates vary by age range. There are flat-rate discounts ($10) on specific days (1 and 6) for people above 12 who are not staying overnight.
    Overnight attenders fall into two groups: full week overnight and specific day overnight.
        Accommodations prices/options are based on age, with the following structure:
            accommodation type
            age range (lower and upper ages inclusive)
            full week price
            daily attender price
    Meals costs are only calculated for people attending specific days (not full-week), either overnight or just daytime. There should be one meal charged per day attending. We have two meal costs:
        Age 0-12 $9
        Age 13+  $15

There is a some kind of "tree" of options for people to select (reflected in the calculation logic) that would make fee calculation a bit more linear/maintainable, such as the following possibility:

    enter registrant age (used in subsequent select steps and final calculation)
    select "Attending Memorial Meeting only?" -
        Yes (true): bypasses all other accommodations and meal choices
        No (false): show "full-week / specific days" option
    select "Attending full week?"
        Yes (true): used in price calculation
        No (false): show "select days attending"
    select "days attending" (optional based on previous condition)
    select "Need overnight accommodations?"
        Yes (true): show accommodations options
        No (false): accommodations are not calculated into registration price
    Program selection (e.g. Children's Program, JYM, YAF)
        options in this field are determined by age eligibility, but do not affect registration cost

Further reading:
https://docs.djangoproject.com/en/3.0/ref/forms/fields/#booleanfield
https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/

https://www.adagio.com/
https://www.adagio.com/green/genmai_cha.html