# Escreva um programa que receba uma lista de números e encontre o maior valor nela.

def searchBiggest(list):
    output = list[0]
    i = 1
    leng = len(list)
    while(i < leng):
        if(list[i] > output):
            output = list[i]
            i += 1
            continue
        i += 1
    return output

print(searchBiggest([-50, -1, 0]))
print(searchBiggest([0, 0, 0]))
print(searchBiggest([1, 2, 0]))