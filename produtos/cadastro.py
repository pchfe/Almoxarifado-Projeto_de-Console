from filtros.filtro import filtrar_produto_tipo


def almoxarifado_cadastro(usuarios, usuarios_logados, produtos): #nome, descricao, tipo, quantidade
    print('\n===== Cadastro de produtos =====\n')
    nome = input('Nome do produto: ')
    descricao = input('Descricao: ')
    tipo = input('Tipo: ')
    quantidade = int(input('Quantidade: '))
    quem_recebe = input('Quem recebe? ')
    
    validar = filtrar_produto_tipo(nome, descricao, tipo, quantidade, quem_recebe)
    if validar:
        menu = int(input('Pesquisar por:\n1. Tipo\n2. Quem recebe\n==> '))
        if menu == 1:
            print(produtos['tipo'])
            print('produtos')