# Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário para adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto.

from random import randint

def rollNum():
    random = randint(1, 100)
    print("ACERTE O NUMERO")
    choice = int(input("Escolha um numero de 1 a 100: "))

    isCorrect = False
    if(choice == random):
        print("PARABENS! VOCE ACERTOU O NUMERO ALEATORIO!")
        return True
    
    while(not isCorrect):
        if(choice > random):
            print("MENOR!")
            choice = int(input("ESCOLHA OUTRO NUMERO: "))
        elif(choice < random):
            print("MAIOR!")
            choice = int(input("ESCOLHA OUTRO NUMERO: "))
        else: 
            print("PARABENS! VOCE ACERTOU O NUMERO ALEATORIO!")
            isCorrect = True
         
rollNum()