# Escreva um programa que receba dois números e uma operação (+, -, *, /) e exibe o resultado.

def calc(a, operator, b):
    if(operator == '+'):
        return a + b
    if(operator == '-'):
        return a - b
    if(operator == '*'):
        return a * b
    if(operator == '**'):
        return a ** b
    if(operator == '/'):
        return a / b
    if(operator == '%'):
        return a % b
    if(operator == '='):
        return a == b
    else: return "error"
    
print(calc(10, "**", 2))
print(calc(10, "/", 2))


