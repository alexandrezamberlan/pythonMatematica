# INSTRUÇÃO WHILE
#  https://www.w3schools.com/python/python_while_loops.asp

# TODA REPETIÇÃO OBEDECE 3 SITUAÇÕES:
  # A - inicialização da variável de controle
  # B - transformação da variável de controle
  # C - uso da variável de controle na condição de parada/continuação

i = 1          #A
while i < 6:   #C
  print(i)
  i += 1       #B

  
# rotina que exibe o i de 1 a 5
# i = 1   #inicialização da variável de controle.
# while (i < 6): #uso da variável de controle na condição de parada.
#   #conjunto de código que quer repetir 5 vezes
#   print(f"repetindo a {i}ª vez")
#   i += 1  #transformação da variável de controle.


# rotina que recebe nomes de pessoas (convertidas em maiúsculo),
# inseridas no final da lista, enquanto o usuário desejar repetir
# lista = []  
# opcao = '1'
# while (opcao == '1'):
#   nome = input("Digite seu nome: ")
#   lista.append(nome.upper())
#   opcao = input("Digite 1 para continuar; qualquer tecla para sair: ")

# print(lista)


# rotina que cadastra qtd amigos na lista meus_amigos
# qtd = int(input("Quantos amigos quer cadastrar? "))
# i = 0
# meus_amigos = []
# while (i < qtd):
#   nome = input("Digite o nome de um amigo: ")
#   meus_amigos.append(nome)
#   i += 1
# print(meus_amigos)

#rotina que popula randomicamente uma lista (tamanho 10) com números inteiros de -100 a 100

from random import random
from random import randint

lista = []
i = 0
while (i < 10):
  #valor = random() #sorteia numeros de 0 a 1
  valor = randint(-100,100) #sorteando números entre -100 a 100
  lista.append(valor) #inserindo valor sorteado na lista
  i += 1

print("Lista gerada aleatoriamente!!")
print(lista)


#rotina que localize o menor valor da lista
menor = lista[0] #estamos assumindo que o menor é o primeiro da lista
i = 0  #incialização da variável de controle
while (i < len(lista)): #teste de parada
  if (lista[i] < menor):
    menor = lista[i]
    
  i += 1 #transformação da variável de controle

print(f"O {menor} foi o menor valor encontrado")


#rotina que localize o maior valor da lista
maior = lista[0]
i = 0  #incialização da variável de controle
while (i < len(lista)): #teste de parada
  if (lista[i] > maior):
    maior = lista[i]
    
  i += 1 #transformação da variável de controle

print(f"O {maior} foi o maior valor encontrado")


#rotina que calcule e exiba a média dos números
soma = 0
i = 0  #incialização da variável de controle
while (i < len(lista)): #teste de parada
  soma = soma + lista[i]  #acumulando item por item em soma
  i += 1

print(f"A média dos valores sorteados é {soma/len(lista)}")

#rotina que recebe um numero inteiro e exibe a sequencia dele ate 0.
numero = int(input("Digite um número: ")) 
while (numero > 0):
  print(numero)
  numero -= 1

#rotina que recebe do usuario quantas notas ele deve informar e recebe os valores das notas (0 a 10), sempre repetindo as notas invalidas. Ao final, deve mostrar a média dessas notas

quantidade_notas = int(input("Digite quantas notas irá cadastrar: "))
i = 0
soma = 0
while (i < quantidade_notas):
  nota = -1 #forçando para que entre no proximo while
  while (nota < 0 or nota > 10):
    nota = float(input(f"Digite a sua {i+1}ª nota [0 a 10]: "))
  
  soma = soma + nota
  i += 1

print(f"A média das notas é {soma/quantidade_notas}")


  
# INSTRUÇÃO FOR
# https://www.w3schools.com/python/python_for_loops.asp
