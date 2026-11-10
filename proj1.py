adicionar = []


while True:
    print('====== MINI CAIXA ======')
    print('-------------------------')

    print('1 - adicionar produto')
    print('2 - ver produtos ')
    print('3 - ver total')
    print('4 - remover produto')
    print('5 - atualizar produto')
    print('0 - sair')
    entrada = int(input('DIGITE O QUE DESEJA FAZER: '))


    #ADICIONAR PRODUTOS E OS VALORES DELES
    if entrada == 1:
        print('== ADICIONAR PRODUTO ==')
        produtos = input('digite qual produto deseja acrescentar: ')
        if produtos.strip() == '':
            print('NOME INVÁLIDO')
        else:
            preco = float(input('digite o valor do produto: '))

        #VALIDAÇÃO PREÇO E QUANTIDADES 
            if preco < 1:
                print('valor invalido')
            else:
                quantidade = int(input('digite a quantidade desses produtos: '))
                if quantidade < 1:
                    print('quantidade invalida')
                else:
                    subtotal = preco * quantidade
                    adicionar.append([produtos, preco, quantidade, subtotal])

    #VER OS PRODUTOS QUE FORAM DICIONADOS E O VALOR DE CADA UM
    elif entrada == 2:
        print('ver produtos')
        print('==== PRODUTOS ====')
        if adicionar == []:
            print('NENHUM PRODUTO ENCONTRADO')
        else:
            for i in range(len(adicionar)):
                print(f'{i + 1} {adicionar[i][0]} | R${adicionar[i][1]:.2f} | Qtd: {adicionar[i][2]} | Subtotal: R${adicionar[i][3]:.2f} ')

    #VER A SOMA DOS VALORES DOS PRODUTOS ADICIONADOS
    elif entrada == 3:
        if adicionar == []:
            print('NENHUM PRODUTO ENCONTRADO')
        else:
            total = 0
            for i in adicionar:
                total = total + i[3]
            print(f'o total da compra é R${total:.2f}')

    #REMOVER PRODUTOS
    elif entrada == 4:
        if adicionar == []:
            print('NENHUM PRODUTO ENCONTRADO')
        else:
            remove = int(input('Digite o numero do produto que deseja remover: '))
            if remove > 0 and remove <= len(adicionar):
                    indice = remove - 1
                    print(f'o produto {adicionar[indice][0]} foi removido. (QTD: {adicionar[indice][2]}).  subtotal:{adicionar[indice][3]} ')
                    adicionar.pop(indice)
            else:
                print('produto invalido')

    #ATUALIZAR PRODUTOS            
    elif entrada == 5:
        if adicionar == []:
            print('NENHUM PRODUTO CADASTRADO')
        else:
            for i in range(len(adicionar)):
                print(f'{i + 1} | {adicionar[i][0]}')
            num_att = int(input('Qual produto deseja atualizar? '))
            if num_att > 0 and num_att <= len(adicionar):
                print('escolha é valida')
                indice = num_att - 1
                print(adicionar[indice][0])
                new_qtd = int(input('Digite a quantidade atualizada: '))
                if new_qtd <1:
                    print('quantidade invalida')
                else:
                    print('quantidade valida')
                    adicionar[indice][2] = new_qtd
                    new_sb = new_qtd * adicionar[indice][1]
                    adicionar[indice][3] = new_sb
                    print('===== ALTERAÇÃO FEITA COM SUCESSO')
                    print(f'A nova quantidade do {adicionar[indice][0]} é {adicionar[indice][2]} e seu novo subtotal é {adicionar[indice][3]}')
            else:
                print('escolha invalida')


    #COMANDO PARA ENCERRAR O CÓDIGO
    elif entrada == 0:
        saida = str(input('tem certeza que deseja sair? (s/n): ')).lower()
        if saida == 's':
            break
        elif saida == 'n':
            print('retornando ao menu...')
            
        else:
            print('opcao invalida')
