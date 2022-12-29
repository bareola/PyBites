names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries(names=names, countries=countries):
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    number = 1
    space = " "
    for number in range(len(names)):
      print (f'{number+1}. {names[number]}{space*(11-len(names[number]))}{countries[number]}')

enumerate_names_countries(names, countries)