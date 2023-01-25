def freq_digit(num: int) -> int:
    list_num = {}
    mostFreq = []
    for i in str(num):
        if i not in list_num:
            list_num[i]=1
        else:
            list_num[i]+=1
    
    for item, value in list_num.items():
        if mostFreq == [] or mostFreq[1] < value:
            mostFreq = [item, value]
    return int(mostFreq[0])

print (freq_digit(199999988231824))