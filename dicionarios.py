gameFifa = {
    "name" : "Fifa 23",
    "gamePrice" : 90.99,
    "classification" : 8.5,
    "genere" : ["esporte","família"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

#recuperar elementos do dicionario

print(gameFifa['genere'])
print(gameFifa.get('classification'))

# buscar chaver do dicionario

print(gameFifa.keys())

#apenas recuperar valores do dicionario
print(gameFifa.values())

#buscar com chave e valor
print(gameFifa.items())

#adiciona item a lista
gameFifa["players"] = 2
print(gameFifa)

# Atualiza item
gameFifa.update({"players":4})
print(gameFifa)