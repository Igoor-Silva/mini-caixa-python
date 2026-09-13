adicionar = []


while True:
    print('====== MINI CAIXA ======')
    print('-------------------------')

    print('1 - adicionar produto')
    print('2 - ver produtos ')
    print('3 - ver total')
    print('4 - remover produto')
    print('0 - sair')
    entrada = int(input('DIGITE O QUE DESEJA FAZER: '))


    #ADICIONAR PRODUTOS E OS VALORES DELES
    if entrada == 1:
        print('adicionar produto')
        produtos = str(input('digite qual produto deseja acrescentar: '))
        preco = float(input('digite o valor do produto: '))
        quantidade = int(input('digite a quantidade desses produtos: '))
        subtotal = preco * quantidade
        adicionar.append([produtos, preco, quantidade, subtotal])

    #VER OS PRODUTOS QUE FORAM DICIONADOS E O VALOR DE CADA UM
    elif entrada == 2:
        print('ver produtos')
        print('==== PRODUTOS ====')
        for i in adicionar:
            print(f'{i[0]} | R${i[1]:.2f} | Qtd: {i[2]}| Subtotal: R${i[3]:.2f}')

    #VER A SOMA DOS VALORES DOS PRODUTOS ADICIONADOS
    elif entrada == 3:
        total = 0
        for i in adicionar:
            total = total + i[3]
        print(f'o total da compra é R${total:.2f}')

    elif entrada == 4:
        remove = int(input('Digite o produto que deseja remover: '))


    #COMANDO PARA ENCERRAR O CÓDIGO
    elif entrada == 0:
        break
    else:
        print('opcao invalida')