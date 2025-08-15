gameSet = {"Fifa 23","PES","Bomba Patch"}
# - Nâo deixa recuperar valores via fatiamento

print(len(gameSet))


# - True e o 1 são considerados 
exampleSet = {"Fifa 23", True, 1,90.50}
print(exampleSet)

gameSet.update(exampleSet)
print(gameSet)