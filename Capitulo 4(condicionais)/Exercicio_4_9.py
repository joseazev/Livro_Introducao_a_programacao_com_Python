imovel = float(input('Qual é o valor do imóvel? '))
salario = float(input('Qual é o salario do comprador? '))
tempo = int(input('Informe o numero de parcelas: '))

ponto_de_corte = salario * 0.3
prestacao = imovel / tempo

print(f'valor: R$: {prestacao:5.2f}')
print(f'Quantidade de prestação {tempo}')

if prestacao < ponto_de_corte:
    print('Aprovado')
else:
    print('Não atende ao critério')
    print(f'Valor para financiamento sugerido é {ponto_de_corte * tempo}')
