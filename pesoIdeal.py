sexo = input("Qual seu sexo? ")
altura =float(input("Qual sua altura? (em metros):  "))

if (sexo== 'mulher'):
    pesoIdeal =float(62.1*altura - 44.7)
    print("Peso ideal é de: ",pesoIdeal)

elif (sexo== "homem"):
    pesoIdeal=float(72.7*altura - 58)
    print("Peso ideal é de: ",pesoIdeal)
