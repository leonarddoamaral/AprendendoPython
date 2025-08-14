string = input("Insira um texto:\n")
pLetra = string[:1]
print(pLetra)
result = string.replace(pLetra,"$")
print(pLetra+result[1:])