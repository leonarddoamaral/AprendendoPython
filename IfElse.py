a = input("Insira um valor para a variavel a:")
b = input ("Insira um valor para a variavel b:")

if (a>b):
    aux = a;
    a=b;
    b= aux;
print("O valor de A agora é...", a);
print("O valor de B agora é...", b);
