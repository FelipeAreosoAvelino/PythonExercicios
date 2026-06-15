#jeito simples igual video
# salario = float(input('Qual é o salário do funcionário? R$'))
# salario_atual = salario + (salario * 0.15)
# print('Um funcionário que ganhava {}, com 15% de aumento, passa a receber {:.2f}'.format(salario, salario_atual))

#Jeito resenhudo
salario = float(input('Qual é o salário do funcionário? R$'))
aumento = float(input('Qual é a porcentagem de aumento salarial do funcionário? '))
salario_atual = salario + (salario*aumento/100) # ou (salario * (aumento * 0.01))
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}'
      .format(salario,aumento, salario_atual))