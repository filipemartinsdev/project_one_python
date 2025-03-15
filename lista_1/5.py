# entender o input (idade)
# se 0 < idade <= 12: crianca
# se 12 < idade <= 17: adolescente
# se 17 < idade <= 59: adulto
# se 59 < idade: idoso

def checkAge(n):
    if(n <= 0): return "error"
    elif(n <= 12): return "crianca"
    elif(n > 12 and n <= 17): return "adolescente"
    elif(n > 17 and n <= 29): return "adulto"
    else: return "idoso"
print(10)
print(100)
print(18)

