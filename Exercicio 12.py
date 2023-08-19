carros_vendidos=int(input("digite o quanto de carro que voce vendeu:"))
total_vendas=float(input("digite o total de vendas:"))
sal_fixo=float(input("digite o seu salario:"))
comissao=float(input("digite a comissao:"))
sal_final=sal_fixo+(comissao*carros_vendidos)+(5*total_vendas/100)

print("o salario final eh de: R$"+str(sal_final))