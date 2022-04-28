print("Programa para IMC")
peso = float( input("Qual o seu peso em kg? ") )
altura = float( input("Qual sua altura em m? ") )
imc = peso / (altura * altura)

print(f"Seu IMC é de {imc}")

if (imc < 18.5):
    print("Você está abaixo do peso")
elif (imc < 24.9):
    print("Você está com peso normal")
elif (imc < 29.9):
    print("Você está com sobrepeso")
elif (imc < 39.9):
    print("Você está obeso")
else:
    print("Você está com obesidade grave")