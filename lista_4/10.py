# Escreva um programa que receba duas listas de números e retorne uma nova lista onde cada elemento é o produto dos elementos correspondentes das duas listas.

def productList(listA, listB):
    if (len(listA) != len(listB)):
        return ValueError
    leng = len(listA)
    output = []
    i = 0
    while(i<leng):
        output.append(listA[i] * listB[i])
        i += 1
    return output

print(productList([1, 2, 3], [1, 2, 3]))