salario = float(input("Insira seu salario atual: "))
gratificacao = float(salario*0.05)
imposto= float(salario*0.07)

novoSalario= float(salario-imposto+gratificacao)
print("Salario antigo: ",salario, "\nGratificação(5%): ",gratificacao,"\nImposto(7%): ",imposto,"\nSalario atual: ",novoSalario)
