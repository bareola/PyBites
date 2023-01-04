import string
def remove_punctuation(input_string):
    punct = string.punctuation
    for x in punct:
        input_string = input_string.replace(x, "")
        print (input_string)
    return input_string