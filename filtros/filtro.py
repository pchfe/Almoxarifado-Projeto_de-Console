

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios['cpf'] if usuario == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def filtrar_instituicao(instituicao, usuarios):
    return instituicao in ['1', '2']

def filtrar_produto_recebe(quem_recebe, produtos): ##PARA CONSULTAS POR DEPARTAMENTO (quem_recebe)
    validar = [validar for validar in produtos['quem_recebe'] if validar == quem_recebe]
    return validar[0] if validar else None

def filtrar_produto_tipo(tipo, produtos): ##PARA CONSULTAS POR TIPO DE PRODUTOS (tipo)
    validar = [validar for validar in produtos['tipo'] if validar == tipo]
    return validar[0] if validar else None

### EXIBIR PRODUTOS CADASTRADOS ###
def exibir_produtos_geral(usuarios, produtos):
    # produtos = {'nome': [], 'descricao': [], 'tipo': [['Camiseta', 'Garrafinha']], 'quantidade': [], 'quem_recebe': []}
    for i, geral in enumerate(produtos['nome']):
        print(f'\nProduto {i+1}: ', produtos['nome'][i], '\nDescrição: ', produtos['descricao'][i], '\nTipo: ', produtos['tipo'][i], '\nQuantidade: ', produtos['quantidade'][i], '\n')

def exibir_produtos_consulta(usuarios, produtos):
    nome = input('Qual produto está buscando?\n==> ')
    consulta_encontrada = []
    for i, consulta in enumerate(produtos['nome']):
        if consulta == nome:
            consulta_encontrada.append(i)
    
    if consulta_encontrada:
        print(len(consulta_encontrada), ' encontrados:\n')
        for j in consulta_encontrada:
            print('\nProduto: ', produtos['nome'][j], '\nTipo: ', produtos['tipo'][j], '\nQuantidade: ', produtos['quantidade'][j], '\n')
    else:
        print('@@@ Ops! Não encontramos este produto no sistema. @@@\n ')

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