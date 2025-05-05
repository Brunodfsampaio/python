preco = 1000 # valor do produto
desconto = 15 # percentual de desconto

valor_final = preco-(preco*desconto/100) # cálcuclo do desconto
print(f"o preço final com {desconto} de desconto é R${valor_final}")
# O f transforma a string em uma f-string (formatted string). Isso permite que você insira variáveis diretamente dentro do texto sem precisar usar + para concatenar.

#Sem f-string (forma antiga):
    # print("O preço final com " + str(desconto) + "% de desconto é R$" + str(valor_final))

#Com f-string (forma moderna e mais legível):
    #print(f"O preço final com {desconto}% de desconto é R${valor_final}")


#A f-string faz com que qualquer variável dentro de {} seja substituída pelo seu valor automaticamente.

