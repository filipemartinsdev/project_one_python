# Escreva uma função que receba o peso (em kg) e a altura (em metros) de uma pessoa e retorne seu IMC. A função deve ser modular para ser usada em diferentes contextos onde seja necessário calcular o IMC.

# IMC = peso (kg) / altura ** 2 (m)

def calcIMC(weight, high):
    result = weight / high ** 2
    return result

def handleIMC(IMC):
    if(IMC < 18.5):
        return "baixo peso"
    elif(IMC < 25):
        return "normal"
    elif(IMC < 30):
        return "sobrepeso"
    else: return "obesidade"