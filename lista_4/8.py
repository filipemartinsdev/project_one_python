# Escreva um programa que receba uma lista e retorne uma nova lista sem elementos duplicados.

def nonDuplicateList(list):
    output = []
    for i in list:
        if(i in output):
            continue
        output.append(i)
    return output

print(nonDuplicateList([1, 2, 2, 3, 4, 4]))
print(nonDuplicateList([10, 10, 10, 10, 0, None]))
print(nonDuplicateList(["py", "js", "js", "py", "py", "ts"]))