def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    if up == True:
        return int(transactions+1)
    else:
        return int(transactions)