peso = float(input("Qual seu peso?: "))
altura = float(input("Qual sua altura?: "))

imc = peso / (altura * altura)
print(imc)
if imc <= 18.5:
    print("Você esta abaixo do peso")
elif imc <= 24.9:
    print("Este é o Peso ideal")
elif imc <= 29.9:
    print("Você esta acima do peso obesidade grau 1")
elif imc <= 34.9:
    print("Voce esta acima do peso obesidade grau 2")
elif imc >= 40:
    print("você esta acima do peso obesidade grau 3")
