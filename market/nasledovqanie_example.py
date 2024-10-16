
class Person:
    """Класс для личности"""
    salary = 0

    def __init__(self, name_pm):
        self.name = name_pm

    def calc_food_money(self):
        return 0

    def calc_clothes_money(self):
        return 0

    def calc_petrol_money(self):
        return 0

    def calc_rent_flat_money(self):
        return 0

    def additional_money(self):
        return 0

    def spend_money_in_month(self):
        food = self.calc_food_money()
        rent = self.calc_rent_flat_money()
        clothes = self.calc_clothes_money()
        petrol = self.calc_petrol_money()
        additional = self.additional_money()
        return self.salary - food - rent - clothes - petrol + additional