a_parede=float(input("digite a altura da parede:"))
l_parede=float(input("digite a largura da parede:"))
a_azulejo=float(input("digite a altura do azulejo:"))
l_azulejo= float(input("digite a largura do azulejo:"))
area_parede=a_parede*l_parede
area_azulejo=a_azulejo*l_azulejo
quant_azulejo=area_parede/area_azulejo

print("a quantidade necessária de azulejo para uma parede eh de "+str(quant_azulejo)+" azulejos")