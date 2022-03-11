"""
*** Recipe Book ***
User requests ingredients list from list of meals.
"""

SEPARATOR = '----------------------'
MEALS = {
    'tacos': ('beef', 'tortillas', 'lettuce'),
    'chicken noodle soup': ('chicken', 'noodles'),
}


def print_meals():
    for meal in MEALS:
        print(meal.title())


def print_options():
    print(f'\n{SEPARATOR}')
    print('Your meal options are:\t')
    print_meals()
    print(SEPARATOR)


print('\nWelcome to your recipe book!')
print_options()
selection = input('\nWhat meal do you want to make?\t').lower()


while selection not in MEALS:
    print('\n*** Option not in recipe book! ***')
    print_options()
    selection = input('\nWhat meal do you want to make?\t').lower()


if selection in MEALS:
    print(f'\n*** {selection.title()} ***')
    for ingredients in MEALS[selection]:
        print(f'\u00B7 {ingredients.title()}')
