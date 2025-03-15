# mostrar qual o maior entre dois inputs (int)

def letBiggest(a, b):
    if(a < b):
        return b
    elif(a == b):
        return "both"
    else: return b
    
print(letBiggest(10, -10))
print(letBiggest(-10, -10))