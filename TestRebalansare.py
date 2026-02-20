import matplotlib.pyplot as plt
from OperatiiActiuni import Actiuni

acty=[1,3,0.666666,2.5,0.8,1.75,0.8571,1.5,0.888888,1.25]
actx=[1,1,4,0.75,2,0.833333,1.6,0.875,1.2857,1.111111]
actnofluc=[1,2,1.5,1.33333,1.25,1.2,1.16666,1.142857,1.125,1.111111]

#multipliers_a = [1,1.1287763278107714, 1.258040307924781, 1.1761812126369053, 0.8519554883973774, 1.0942118059104813, 0.9765698369936763, 0.997166765909398, 0.8986678819502176, 0.9931081112786669, 1.1832613764313857, 0.839356502594551, 1.0150973797447869]

#multipliers_b = [1,1.381925714672318, 1.02031453847481, 1.0147257667057208, 1.1677849299778127, 1.0849921367389719, 1.021408685603764, 1.3603800790467704, 0.7624959667693549, 1.0187579529891921, 0.999834243518235, 0.6976227131823111, 0.8821502699037378]

multipliers_a = [1.1287763278107714, 1.258040307924781, 1.1761812126369053, 0.8519554883973774, 1.0942118059104813, 0.9765698369936763, 0.997166765909398, 0.8986678819502176, 0.9931081112786669, 1.1832613764313857]

multipliers_b = [1.381925714672318, 1.02031453847481, 1.0147257667057208, 1.1677849299778127, 1.0849921367389719, 1.021408685603764, 1.3603800790467704, 0.7624959667693549, 1.0187579529891921, 0.999834243518235]

#Actiuni.DictionarFluctuatiiActiuni["y"]=acty
#Actiuni.DictionarFluctuatiiActiuni["fluc"]=actnofluc
#Actiuni.DictionarFluctuatiiActiuni["x"]=actx

Actiuni.DictionarFluctuatiiActiuni["a"]=multipliers_a
Actiuni.DictionarFluctuatiiActiuni["b"]=multipliers_b

Actiuni.luni=10
Actiuni.buget_initial=1
Actiuni.buget_lunar=1

a=Actiuni.valori_actiune("a",1,1)
b=Actiuni.valori_actiune("b",1,1)
#fluc=Actiuni.valori_actiune("fluc",1,1)

line=list(range(10))

portofoliu=Actiuni.rebalansare()

plt.plot(line,a)
plt.plot(line,b)
#plt.plot(line,fluc)
plt.plot(line,portofoliu,label="Rebalans")
plt.legend(loc="lower right")
plt.show()

valori=[1,2,6,24]
fluctuatii=Actiuni.convertire_valori(valori)
print(fluctuatii)
Actiuni.luni=4
Actiuni.DictionarFluctuatiiActiuni["fluctuatii"]=fluctuatii
print(Actiuni.valori_actiune("fluctuatii", 1,0))
