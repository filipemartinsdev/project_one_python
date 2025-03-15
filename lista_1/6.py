# [

# esta errado.

def isLeapYear(n):
    if(n % 4 == 0):
        return True
    elif(n % 400 == 0):
        return True
    else: return False
    
print(isLeapYear(1999))