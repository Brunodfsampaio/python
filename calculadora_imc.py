# calculadora de imc
# peso dividido pela altura 

altura = float(input("digite a sua altura em metro:"))
peso = float(input("digite seu peso em kgs:"))

imc = peso / (altura ** 2)

print(f"seu imc é {imc:.2f}")

if imc < 18.5:
    print("abaixo do peso ideal")

if imc < 25:
    print("peso normal")

if imc < 30:
    print("sobrepreso")
else:
    print("acima do peso")