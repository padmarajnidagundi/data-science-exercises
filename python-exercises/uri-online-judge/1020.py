valor = 943
ano = int(valor / 365)
print(ano)
mes = int((valor%365/30))
print("Mês {}".format(mes))
print(valor%365)
dia = int(valor%365%30)
print("Dia {}".format(dia))
print(valor%365%30)

print('%d ano(s)\n%d mes(es)\n%d dia(s)' %(ano,mes,dia))