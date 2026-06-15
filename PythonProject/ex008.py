#variaveis
m = float(input('Digite uma distancia em metros: '))
#code
print('A medida de {} metros corresponde a:\n{:.0f}km \n{:.0f}hm \n{:.0f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm '
      .format(m,(m/1000),(m/100),(m/10),(m*10),(m*100),(m*1000)))