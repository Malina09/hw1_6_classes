import math


class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.lower().capitalize()
        self.last_name = last_name.title()
        self.full_name = self.first_name + ' ' + self.last_name
        self.initials = self.first_name[0] + '. ' + self.last_name[0]


class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self, first_number, second_number):
        return self.first_number + self.second_number

    def subtract(self, first_number, second_number):
        return self.first_number - self.second_number

    def multiply(self, first_number, second_number):
        return self.first_number * self.second_number

    def divide(self, first_nuber, second_number):
        return self.first_number / self.second_number


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, str_to_parse):
        first_name, last_name, salary = str_to_parse.split('-')
        return cls(first_name, last_name, int(salary))


class Pizza:
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])


class Circle:
    def __init__(self, radios=0):
        self.radios = radios

    def get_area(self):
        return math.pi * pow(self.radios, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radios


class Beverage:
    ingredients_cost = {'Strawberries': 1.50,
                        'Banana': 0.50,
                        'Mango': 2.50,
                        'Blueberries': 1.00,
                        'Raspberries': 1.00,
                        'Apples': 1.75,
                        'Pineapple': 3.50}

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        cost = 0
        for i in range(0, len(self.ingredients)):
            if self.ingredients[i] in Beverage.ingredients_cost:
                cost += Beverage.ingredients_cost[self.ingredients[i]]
        return '$' + str(cost)

    def get_price(self):
        cost = 0
        for i in range(0, len(self.ingredients)):
            if self.ingredients[i] in Beverage.ingredients_cost:
                cost += Beverage.ingredients_cost[self.ingredients[i]]
        price = cost * 2.5
        return '$' + str(price)

    def get_name(self):
        sort_list = []
        if len(self.ingredients) > 1:
            sort_list += [self.ingredients[i] for i in range(0, len(self.ingredients))]
            for i in range(0, len(sort_list)):
                if 'Blueberries' in sort_list and sort_list[i] == 'Blueberries':
                    sort_list[i] = 'Blueberry'
                if 'Raspberries' in sort_list and sort_list[i] == 'Raspberries':
                    sort_list[i] = 'Raspberry'
                if 'Strawberries' in sort_list and sort_list[i] == 'Strawberries':
                    sort_list[i] = 'Strawberry'
            print(*sorted(sort_list), 'Fusion')
            return ''
        else:
            if 'Blueberries' in self.ingredients:
                self.ingredients = 'Blueberry'
            if 'Raspberries' in self.ingredients:
                self.ingredients = 'Raspberry'
            if 'Strawberries' in self.ingredients:
                self.ingredients = 'Strawberry'
            print(*self.ingredients, 'Smoothie')
            return ''
