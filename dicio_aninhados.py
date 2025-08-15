import pprint

conjunto = {
    "Mario":{
        "protagonista":"Mario",
        "empresa":"Nintendo",
        "nota": 8.2,
        "personagens":["Bowser","Luighi"]
    },
    "Sonic":{
        "protagonista":"Sonic",
        "empresa":"SEGA",
        "nota": 8.2,
        "personagens":["Tailes","Amy"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(conjunto)
#buscar itens
print(conjunto["Mario"]["personagens"])

#adicionar novo item
conjunto["Mario"]["jogadores"]=1
print(conjunto["Mario"])

#excluir
del conjunto["Sonic"]
pp.pprint(conjunto)