import datetime

# contador = 0 #inicializa o contador
# while contador < 5:  #usa o contador no teste de parada
#   ano = int(input("Digite um ano qualquer: "))
#   if (ano % 4 == 0):
#     print("Ano bissexto!")
#   else:
#     print("Ano normal")

#   contador = contador + 1  #transforma o contador
  


data_horario_atual = datetime.datetime.now()
data = data_horario_atual.date()
ano_atual = data.strftime("%Y")

contador = 0
data_tem_erro = True

while data_tem_erro:

  if (contador == 3):
    print("Você tentou 3 vezes e o sistema será finalizado")
    break;
  else:
    contador = contador + 1
    dia = int(input("Digite um dia válido: "))
    if (dia < 1 or dia > 31):
      print("Dia inválido")
    else:
      mes = int(input("Digite um mês válido: "))
      if (mes < 1 or mes > 12):
        print("Mês inválido")
      else:
        if (dia == 31 and (mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11)):
          print("Data inválida... esse mês não tem 31 dias!!")
        else:
          ano = int(input("Digite um ano válido [aaaa]: "))
          if (ano < 1900 or ano > int(ano_atual)):
            print(f"Ano inválido! Estamos em {ano_atual}")
          else:
              if (dia == 29 and mes == 2 and (ano % 4 != 0)):
                print("Data inválida, pois o ano não é bissexto!")
              else:
                data_tem_erro = False; #se chegou aqui, pq data esta correta
    
