from collections import Counter
def major_n_minor(numbers):
    countNum = Counter(numbers)
    major = countNum.most_common()[0][0]
    minor = countNum.most_common()[-1][0]

    return major, minor