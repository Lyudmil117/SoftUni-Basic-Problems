def krugli_chsla(nachalen_spisuk): # тук функцията кръгли числа ПОЛУЧАВА  нещо(начален списък)
iskan_spisuk = list()
    for n in nachalen_spisuk:
        kruglo = round(float(input()))
        iskan_spisuk.append(kruglo)
    return iskan_spisuk


nachalen_spisuk = input().split(" ")
print(krugli_chsla(.....))
