# Escreva um programa que receba \( N \) números do usuário e calcule a média deles

def media(*args):
    output = 0
    count = 0
    for i in args:
        output += i
        count += 1
    output = output / count
    return output

print(media(6, 6, 6))
print(media(3, 6, 9))
print(media(4, 8, 24))
