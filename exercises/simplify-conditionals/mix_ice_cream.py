# by Kami Bigdely
# Consolidate duplicate conditional fragments

def add(mix, ingrediants):
    mix.append(ingrediants)
    return mix


def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']


def if_milkskake(drink):
    return 'strawberry milkshake' in drink


def if_coffee(drink):
    return 'coffee' in drink


def make_drink(drink, addons):
    mix = []

    if if_coffee(drink):
        mix = add(mix, 'coffee')
        mix = add(mix, addons)
    if if_milkskake(drink):
        mix = mixer_ice_with_cream()
        mix = add(mix, 'strawberry')
        mix = add(mix, addons)
    return mix


final_drink = make_drink('strawberry milkshake', ['milk', 'sugar'])
print(final_drink)
