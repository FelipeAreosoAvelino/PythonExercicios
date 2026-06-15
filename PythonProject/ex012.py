#var
preco = int(input('Qual é o preço do produto? R$'))
#--------------forma igual a do video:-------
# print('O produto que custava R${}, na promoção com desconto de 5% vai custar {}'
#       .format(preco, (preco - (preco * 0.05 ou preco *5/100))))
#--------------forma resenha-----------------

desconto = int(input('Qual é a porcentagem de desconto? '))
valor_desconto = preco * (desconto * 0.01)# preco - (preco * desconto / 100)
print('O produto que custava R${}, na promoção com desconto de {}% vai custar {:.2f}R$'
       .format(preco, (desconto * 1),(valor_desconto)))