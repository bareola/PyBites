def freq_digit(num: int) -> int:
    list_num = {}
    mostFreq = []
    for i in str(num):
        if i not in list_num:
            list_num[i]=1
        else:
            list_num[i]+=1
    return int(max(list_num, key=list_num.get))

# def freq_digit(num: int) -> int:
#     return int(max(str(num), key=str(num).count))