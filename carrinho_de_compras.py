def titulo(texto):
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)


catalogo = {"camiseta": 49.90, "calca": 120.00, "tenis": 250.00, "bone": 29.90}
carrinho = []
cupons_usados = set()

while True:
    titulo('  CARRINHO DE COMPRAS  ')
    
    print('[1] Ver catalógo\n' \
    '[2] Adicionar produto ao carrinho\n' \
    '[3] Ver carrinho e valor total\n' \
    '[4] Aplicar cupom de desconto\n' \
    '[5] Finalizar compra / Sair')

    try:
        opcao = int(input('Opção: '))
    except ValueError:
        print('Somente números.')
        continue

    if len(str(opcao)) != 1:
        print('Somente 1 caractere.')
    elif opcao not in [1, 2, 3, 4, 5]:
        print('Somente números: 1, 2, 3, 4 ou 5.')

    elif opcao == 1:
        titulo('  CATÁLOGO  ')
        for produto, preco in catalogo.items():
            print(f'{produto} - {preco:.2f}') 

    elif opcao == 2:
        titulo('  ADICIONAR ITENS AO CARRINHO  ')
        tentativas = 3

        while tentativas > 0:
            nome_produto = input('Nome para adicionar: ')
            if nome_produto in catalogo:
                carrinho.append(nome_produto)
                print(f'{nome_produto} adicionado ao carrinho!')
                break
            else:
                tentativas -= 1
                print(f'Ops! Não temos esse item no catálogo. Você tem [{tentativas} tentativas].')

    elif opcao == 3:
        titulo('  SEU CARRINHO  ')
        total = 0
        for item in carrinho:
            print(item)
            total += catalogo[item]

        print(f'VALOR TOTAL: {total:.2f}')

    elif opcao == 4:
        cupom_valido = 'PYTHON10'
        cupom_digitado = input('CUPOM: ').upper()
        if cupom_digitado == cupom_valido:
            if cupom_digitado in cupons_usados:
                print('Esse cupom já foi usado! ')
            else:
                total = 0
                for item in carrinho:
                    total += catalogo[item]
                
                preco_final = total * 0.90
                print(f'TOTAL: R${total:.2f}')
                print('CUPOM APLICADO: PYTHON10')
                print(f'VALOR FINAL: {preco_final:.2f}')
            cupons_usados.add(cupom_digitado)
        else:
            print('Cupom inválido')

    elif opcao == 5:
        print('Compra finalizada.')
        break
        