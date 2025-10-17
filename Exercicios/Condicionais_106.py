"""Entrar com um nome e imprimi-lo se o primeiro caractere for a letra A
(considerar letra minúscula ou maiúscula)."""


import os
os.system('cls')

nome = input("Insira o nome: ")

if(nome[0].upper()=='A'):
    print(f"O nome começa com a letra A {nome}")
else:
    print("Inválido")