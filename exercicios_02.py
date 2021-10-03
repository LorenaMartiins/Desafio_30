import os

nome = input("Digite seu nome:")
peso = float(input("Digite seu peso: (kg) "))
altura = float(input("Digite sua altura: (m) "))

print("------------------------------------")

imc = peso / (altura * altura)

print("O resultado do seu IMC é {:.1f}".format(imc))


if imc < 18.5:
    print("Você esta com MAGREZA!")
elif 18.5 <= imc < 24.9:
    print("Seu imc está NORMAL!")
elif 25.0 <= imc < 29.9:
    print("Você está com SOBREPESO!")
elif 30.0 <= imc < 39.9:
    print("Você está com OBESIDADE!")
else:
    print("Você está com OBESIDADE GRAVE!!")

os.system("pause")