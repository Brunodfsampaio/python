numero_inteiro = 25
print(f"Inteiro: {numero_inteiro}, tipo: {type(numero_inteiro)}")

"""

print(f"Inteiro: {numero_inteiro}, tipo: {type(numero_inteiro)}")
O print() é uma função que exibe informações na tela. Vamos dividir essa linha para entender melhor:

🔹 f"Inteiro: {numero_inteiro}, tipo: {type(numero_inteiro)}"

O f antes das aspas (f"...") indica uma f-string (string formatada).

O que estiver dentro de {} será substituído pelo valor real da variável.

🔹 {numero_inteiro} Isso pega o valor da variável numero_inteiro, que é 25, e insere no texto da mensagem.

🔹 {type(numero_inteiro)} Aqui estamos chamando a função type(), que mostra qual é o tipo de dado da variável. No caso, numero_inteiro é um inteiro (int), então type(numero_inteiro) retorna <class 'int'>

"""

numero_float = 3.14159
print(f"Float: {numero_float}, tipo {type(numero_float)}")

texto = "Estou Aprendendo Python"
print(f"String ou Texto: {texto}, tipo: {type(texto)}")

esta_chovendo = False  # Booleano
print(f"Booleano: {esta_chovendo}, tipo: {type(esta_chovendo)}")

idade_str = "30"  # String
idade_int = int(idade_str)  # Convertendo para inteiro

print(f"Convertendo: {idade_str} do tipo {type(idade_str)} para {idade_int} do tipo {type(idade_int)}")

print(type(numero_float))
print(type(texto))
print(type(esta_chovendo))