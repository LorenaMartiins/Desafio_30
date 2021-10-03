import os

n1 = int(input("Digite aqui sua primeira nota:"))
n2 = int(input("Digite aqui sua segunda nota:"))
n3 = int(input("Digite aqui sua terceira nota:"))

media = (n1+n2+n3) / 3

if media < 6:
    print("Sua média foi:",int(media),"Você não conseguiu atingir a média.","Reprovado/a!!")
else:
    print("Sua média foi:",int(media),"Você conseguiu atingir a média.","Aprovado/a!!")


os.system("pause")