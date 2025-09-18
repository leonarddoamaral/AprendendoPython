from colorama import Fore, Style

excel = [{"Leonardo": 10, "Geovane": 11}]
share = [{"Leonardo": 12, "Geovane": 11}]

i = 0
while i < len(share) and i < len(excel):
    if share[i] != excel[i]:
        print(Fore.RED+f"linha {i} diferente!!!"+Style.RESET_ALL)
        print(Fore.LIGHTRED_EX+f"linha atual share = {share[i]}. linha excel {excel[i]}"+Style.RESET_ALL)
        share[i] = excel[i]
        print(Fore.CYAN+f"linha esperada = share:{share[i]}. linha excel {excel[i]}"+Style.RESET_ALL)
        print("\n Corrigido!")
    i += 1
print("____________________________________________________________________")
print(excel)
print("____________________________________________________________________")
print(share)


