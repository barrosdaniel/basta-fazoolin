import locale
locale.setlocale(locale.LC_ALL, '')

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
   
    def __repr__(self):
        return f"Menu: {self.name}, Availability: {self.start_time} to {self.end_time}."
    
    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            if item in self.items:
                total_price += self.items[item]
        return total_price
    
brunch = Menu('Brunch',
            {'pancakes': 7.50,
            'waffles': 9.00,
            'burger': 11.00,
            'home fries': 4.50,
            'coffee': 1.50,
            'espresso': 3.00,
            'tea': 1.00,
            'mimosa': 10.50,
            'orange juice': 3.50},
            11,
            16)

early_bird = Menu('Early Bird',
                {'salumeria plate': 8.00,
                'salad and breadsticks (serves 2, no refills)': 14.00,
                'pizza with quattro formaggi': 9.00,
                'duck ragu': 17.50,
                'mushroom ravioli (vegan)': 13.50,
                'coffee': 1.50,
                'espresso': 3.00},
                15,
                18)

dinner = Menu('Dinner',
            {'crostini with eggplant caponata': 13.00,
            'ceaser salad': 16.00,
            'pizza with quattro formaggi': 11.00,
            'duck ragu': 19.50,
            'mushroom ravioli (vegan)': 13.50,
            'coffee': 2.00,
            'espresso': 3.00},
            17,
            23)

kids = Menu('Kids',
            {'chicken nuggets': 6.50,
            'fusilli with wild mushrooms': 12.00,
            'apple juice': 3.00},
            11,
            21)

print(brunch)

order1 = ['pancakes']
order2 = ['home fries', 'coffee']

print(locale.currency(brunch.calculate_bill(order1)))
print(locale.currency(brunch.calculate_bill(order2)))

order3 = ['salumeria plate', 'mushroom ravioli (vegan)']
print(locale.currency(early_bird.calculate_bill(order3)))

# =======================
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"Address: {self.address}"
    
    def available_menus(self, time):
        available_menus_list = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus_list.append(menu)
        return available_menus_list

flagship_store = Franchise('1232 West End Road',
                    [
                        brunch,
                        early_bird,
                        dinner,
                        kids
                    ])
new_installment = Franchise('12 East Mulberry Street',
                    [
                        brunch,
                        early_bird,
                        dinner,
                        kids
                    ])

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))
