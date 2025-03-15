# verificar se:
# input == par
# input == impar

def parImp(input):
    if(input % 2 == 0):
        return "par"
    else: return "impar"

print(parImp(10))
print(parImp(-7))
