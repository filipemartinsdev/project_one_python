# Escreva um programa que receba três lados de um triângulo e verifique se eles formam um triângulo válido.

def checkTriangle(a, b, c):
    if(a + b > c and b + c > a and c + a > b): return True
    else: return False 

print(checkTriangle(10, 10, 10))
print(checkTriangle(3, 4, 5))
print(checkTriangle(10, 20, 3))


