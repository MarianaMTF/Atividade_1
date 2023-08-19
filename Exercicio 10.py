idade=int(input("digite a sua idade:"))
meses=int(input("Digite os meses: "))
dias=int(input("Digite os dias: "))
dia_ano=365*idade
dia_meses=30*meses
total=dia_ano+dia_meses+dias

print("sua idade em anos para dias eh:"+str(total)+" dias")