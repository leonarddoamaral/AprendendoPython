arquivo = open('arqText.txt', 'w')

arquivo.write('Curso pynton \n')
arquivo.write('Aula pratica')

arquivo.close()

#ler o arquivo

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()
