NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    sortedNames = []
    for name in names:
        if name.title() not in sortedNames:
            sortedNames.append(name.title())
    return sortedNames

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key=lambda x: x.split()[-1], reverse=True)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortestName = None
    for name in names:
        if shortestName == None:
            shortestName = name.split()[0]
        elif len(name.split()[0])<len(shortestName):
            shortestName = name.split()[0]
    return shortestName
shortest_first_name(NAMES)