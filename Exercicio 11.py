valor_carro=float(input("digite o preco do carro:"))
porc_dist=0.28
porc_imposto=0.45
valor_final=valor_carro+(porc_dist*valor_carro)+(porc_imposto*valor_carro)

print("o valor final do carro eh: R$"+str(valor_final))