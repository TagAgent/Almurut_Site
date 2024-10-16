from market.nasledovqanie_example import Person

class Doctor(Person):
    salary = 55_000

    def calc_food_money(self):
        return 10_000

    def calc_petrol_money(self):
        return 5_500

    def additional_money(self):
        return 1_000_000

d2 = Doctor(name_pm='Доктор артхаус')

print(f'Остаток денег у {d2.name}', d2.spend_money_in_month())
