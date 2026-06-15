#variaveis
n = int(input('Digite um numero: '))
# dobro = n * 2
# triplo = n * 3
# raiz = n**(1/2)
#code
#forma 1
# print('O dobro de {} vale {} \nO triplo de {} vale {} \nO raiz quadrada de {} vale {}'
#.format(n, dobro, n,triplo, n,raiz))
#forma 2
print('O dobro de {} vale {} \nO triplo de {} vale {} \nO raiz quadrada de {} vale {:.3f}'
      .format(n, (n*2), n,(n*3), n,(n**(1/2)))) #ou pow(n, (1/2))