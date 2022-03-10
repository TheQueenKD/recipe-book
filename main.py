"""
as the user ask for the shopping list items for a meal

TODO: if item is not in MEALS -> ask again
"""


MEALS = {
    'tacos': ('beef', 'tortillas', 'lettuce'),
    'chicken noodle soup': ('more goodness', 'hello world'),
}


def print_meals():
    for meal in MEALS:
        print(meal.title())


def print_options():
    print('\nYour meal options are:\t')
    print_meals()


print('\nWelcome to your recipe book!')
print_options()
selection = input('\nWhat meal do you want to make?\t')
lowercase_selection = selection.lower()


if lowercase_selection in MEALS:
    print(f'\n*** {selection.title()} ***')
    for ingredients in MEALS[lowercase_selection]:
        print(f'\u00B7 {ingredients.title()}')
else:
    print('\n*** Option not in recipe book! ***')
    print_options()
