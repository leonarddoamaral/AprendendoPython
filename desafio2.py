pPalavra = input("Insira a primeira palavra:\n")
sPalavra = input("Insira a segunda palavra:\n")

inPrimeira = pPalavra[:2]
inSegunda = sPalavra[:2]

troca1= pPalavra.replace(inPrimeira,inSegunda)
troca2= sPalavra.replace(inSegunda,inPrimeira)

palavra = troca1+" "+troca2
print(palavra)