# Escreva um programa que receba uma lista e um elemento, e conte quantas vezes o elemento aparece na lista.

def searchCountList(list, item):
    leng = len(list)
    output = 0
    i = 0
    while(i < leng):
        if(list[i] == item): output += 1
        i += 1
    return output

print(
    searchCountList(
        [1, 2, "eu", "tu", "eu"],
        "eu"
    )
)