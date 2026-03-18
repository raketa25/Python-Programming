"""
This code defines a function `band_name` that takes two parameters, `pet` and `street`, and returns a string that combines these two parameters in the format "street pet". The function is then called with the variables `first_pet` and `first_street`, which are set to 'Chloe' and 'Obrian', respectively. Finally, the resulting band name is printed to the console.
"""
def band_name(pet, street):
    name = f'{street} {pet}'
    return name

first_pet = 'Chloe'
first_street = 'Obrian'

response = band_name(first_pet, first_street)

print(f'Your Band name is {response}')