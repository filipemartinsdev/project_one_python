# Escreva uma função que receba três números e retorne o maior deles. A função deve ser modular para ser usada em diferentes contextos onde seja necessário encontrar o maior valor entre três números.

def biggestN(*numbers):
    listLen = len(numbers)
    
    output = numbers[0]
    i = 1
    while(i < listLen):
        item = numbers[i]
        if(item > output):
            output = item
        i += 1
    return output
print(biggestN(1, 5, 3, 4))
print(biggestN(-1, -5, -3, -4))
print(biggestN(-0, 1, 3.14, 0.5))

