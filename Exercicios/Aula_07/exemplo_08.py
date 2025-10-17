import os
os.system('cls')
import time


num = int(input("Digite um número: "))
i=2
while (i<=num//2):
    if(num % i==0):
        print(f"{num}Não é primo!!")
        break
    i+=1
else:
    print(f"{num} é primo!!")    