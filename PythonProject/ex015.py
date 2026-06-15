dias = int(input('Por quantos dias o carro foi alugado? '))
km_percorrido = float(input('Quantos km o carro percorreu? '))
preco = 60 * dias + 0.15 * km_percorrido
print('O total a pagar é {:.2f}'.format(preco))