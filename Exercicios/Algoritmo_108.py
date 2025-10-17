#Idem ao anterior, porém considerar: JOSÉ, José ou josé.

import os
os.system('cls')

nome = input("Digite o seu nome: ")

if(nome[:4].upper() in ["JOSÉ","JOSE"]):
    print(nome)
else:
    print("Não começa com 'JOSE'")    