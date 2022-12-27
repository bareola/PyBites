def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    import math
    if up == True:
        return [math.ceil(x) for x in transactions]
    else:
        return [math.floor(x) for x in transactions]