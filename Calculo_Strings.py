# -*- coding: utf-8 -*-
"""Código para calculo de strings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DQCbGC6m90-daK9deaXzb3KRpW48-uKe
"""

#----------------Cálculo para correção de temperatura e quantidade máxima de módulos por string----------------#
voc = float(input("Digite a tensão VOC do módulo:" " "))
cvoc = float(input("Digite o coeficiente de VOC do módulo:" " "))
tmax = voc * (1 + (cvoc / 100) * (10 - 25)) #fórmula para correção da temperatura máxima do módulo#
vmaxinv = int(input("Digite a tensão máxima do inversor:" " "))
qtd_max = round(vmaxinv/tmax)-1

#----------------Cálculo para correção de temperatura e quantidade mínima de módulos por string----------------#
vmp = float(input("Digite a tensão VMP do módulo:" " "))
cvmp = float(input("Digite o coeficiente de VMP do módulo:" " "))
tmin = vmp * (1 + (cvmp / 100) * (70 - 25)) #fórmula para correção da temperatura minima do módulo#
vstart = int(input("Digite a tensão de start da MPPT:" " "))
qtd_min = round(vstart/tmin)+0

#----------------Cálculo para correção da corrente e quantidade máxima de módulos em paralelo----------------#
#isc = float(input("Digite a corrente ISC do módulo:" " "))
#cisc = float(input("Digite o coeficiente de ISC do módulo:" " "))
#cmax = isc * (1 + (cisc / 100) * (70 - 25))
#isc_max = int(input("Digite o ISC máximo do inversor:" " "))
#max_prl = round(isc_max/cmax)-1

#----------------Cálculo para correção da corrente e quantidade mínima de módulos em paralelo----------------#
#imp = float(input("Digite a corrente IMP do módulo:" " "))
#cimp = float(input("Digite o coeficiente de IMP do módulo:" " "))
#cmin = imp * (1 + (cimp / 100) * (10 - 25))
#imp_max = int(input("Digite o IMP máximo do inversor:" " "))
#min_prl = round(imp_max/cmin)+1

#----------------Saída dos resultados----------------#

#print ("temperatura corrigida:" " ", tmax)
#print ("temperatura corrigida:" " ", tmin)
print ("Quantidade máxima de módulos em série:", qtd_max)
print ("Quantidade mínima de módulos em série:", qtd_min)
#print ("Quantidade máxima de strings em paralelo:", max_prl)
#print ("Quantidade mínima de strings em paralelo:", min_prl)