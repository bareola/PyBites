NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
   """Look up name (case insensitive search) and return age.
   If name in > 1 dict, return the match of the group with
   greatest N (so group3 > group2 > group1)"""
   if type(name) != str:
      return NOT_FOUND
   for group in (group3, group2, group1):
      if name.lower() in group:
            return group[name.lower()]
   return NOT_FOUND

print (get_person_age(1))