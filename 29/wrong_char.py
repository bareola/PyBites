def get_index_different_char(chars):
    import string
    alphaNumList = list(string.ascii_letters + string.digits)
    alphaNum = [x for x in enumerate(chars) if str(x[1]) in alphaNumList]
    nonAlpha = [x for x in enumerate(chars) if str(x[1]) not in alphaNumList]
    return alphaNum[0][0] if len(alphaNum) == 1 else nonAlpha[0][0]