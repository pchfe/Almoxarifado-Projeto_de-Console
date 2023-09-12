
def cadastro(usuarios, produtos, usuarios_logados):
    cpf = int(input('Informe o seu CPF completo (apenas números): '))
    
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Ops! Um usuário com este CPF já está cadastrado.')

    user_id = len(usuarios['cpf']) + 1
    usuarios['id'].append(user_id)
    usuarios['nivel'].append(1) #ALTERAR NIVEL DO USUÁRIO
    usuarios['nome'].append(input('Informe o seu nome: '))
    usuarios['cpf'].append(cpf)
    usuarios['senha'].append(input('Informe a sua senha: '))
    print('\nUsuário cadastrado com sucesso!\n')


def login(usuarios, produtos, usuarios_logados, entregas, relatorios):
    print('Entrar: ')
    cpf = int(input('Informe o seu CPF completo (apenas números): '))
    senha = input('Digite a sua senha: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario and senha in usuarios['senha']:
        if usuario in usuarios_logados:
            print('Você já está logado.')
        else:
            usuarios_logados.add(usuario)
            for i, loc in enumerate((usuarios['cpf'])):
                if loc == cpf:
                    print('\nLogin bem sucedido!')
                    nivel = usuarios['nivel'][i] #extrair o nivel de permissão
                    nome = usuarios['nome'][i] #extrarir o nome do usuario logado
                    id_usuario = usuarios['id'][i]
                    filtro = filtrar_nivel(nivel, usuarios)
                    almoxarifado(usuario, filtro, nome, id_usuario, usuarios, produtos, usuarios_logados, entregas, relatorios)
    else:
        print('\nOps! Parece que este CPF não está cadastrado. Tente novamente.\n ')

def fazer_logout(usuario, usuarios, usuarios_logados):
    if usuario in usuarios_logados:
        usuarios_logados.remove(usuario)
        print('\nVocê saiu.\n')
        return
    else:
        print('Você não está logado')

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios['cpf'] if usuario == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def filtrar_nivel(nivel, usuarios):
    nivel_filtrado = [filtro for filtro in usuarios['nivel'] if filtro == nivel]
    return nivel_filtrado[0] if nivel_filtrado else None

def almoxarifado(usuario, filtro, nome, id_usuario, usuarios, produtos, usuarios_logados, entregas, relatorios):
    filtro = filtrar_nivel(filtro, usuarios)
    while True:
        print_menu(filtro, nome)
        if usuario:
            if usuario in usuarios_logados:
                if filtro == 1:
                    menu = int(input('=> '))
                    if menu == 1:
                        add_produto(usuario, id_usuario, produtos)
                    elif menu == 2:
                        entregar(usuario, id_usuario, produtos, entregas, relatorios)
                    elif menu == 3:
                        catalogo(produtos, entregas)
                    elif menu == 4:
                        fazer_logout(usuario, usuarios, usuarios_logados)
                        break
                    else:
                        print('\nOps! Você não tem permissão para acessar esta sessão.\n')
                elif filtro == 2:
                    menu = int(input('=> '))
                    if menu == 1:
                        add_produto(usuario, id_usuario, produtos)
                    elif menu == 2:
                        alter_produto(usuario, usuarios, produtos, usuarios_logados)
                    elif menu == 3:
                        remover_produto(usuario, usuarios, produtos, usuarios_logados)
                    elif menu == 4:
                        entregar(usuario, id_usuario, produtos, entregas, relatorios)
                    elif menu == 5:
                        catalogo(produtos, entregas)
                    elif menu == 6:
                        fazer_logout(usuario, usuarios, usuarios_logados)
                        break
                    else:
                        print('\nOps! Você não tem permissão para acessar esta sessão.\n')
                else:
                    print('Ops! Você não tem permissão suficiente para acessar o almoxarifado.\n')

        else:
            print('\nErro! Faça login para acessar esta página.\n')

def print_menu(filtro, nome):
    print(f'\nOlá, {nome}! - Bem vindo ao Almoxarifado:')
    if filtro == 1:
        print('1. Adicionar produto')
        print('2. Enviar para um departamento')
        print('3. Consultar estoque')
        print('4. Sair do almoxarifado')
    elif filtro == 2:
        print('1. Adicionar produto')
        print('2. Alterar produto')
        print('3. Remover produto')
        print('4. Enviar para um departamento')
        print('5. Consultar o estoque')
        print('6. Sair do almoxarifado')
    else:
        print('\nVocê não tem permissão para acessar o almoxarifado.\n')

def exibir_relatorio():
    pass

def catalogo(produtos, entregas):
    for i, produto in enumerate(produtos['id_produto']):
        print('\nProduto: ', produtos['nome'][i].title(), '\nQuantidade geral: ', produtos['quantidade'][i], '\nDescrição: ', produtos['descricao'][i].title(), '\n')
        if produto in entregas['id_produto']:
            print('\nEntregues:\n--> Secretaria: ', entregas['dep_destino']['secretaria']['quantidade'])
            print('\nEntregues:\n--> Sala: ', entregas['dep_destino']['sala']['quantidade'])
       

def add_produto(usuario, id_usuario, produtos):
    if usuario:
        
        nome_produto = input('Nome do produto: ')
        if nome_produto in produtos['nome']:
            for i, produto_nome in enumerate((produtos['nome'])):
                if nome_produto == produto_nome:
                    print(f'Adicionar mais {nome_produto.title()}:')
                    nova_qtd = int(input('Insira a nova quantidade: '))
                    produtos['quantidade'][i] += nova_qtd
        else:
            print('SESSÃO - ADICIONAR PRODUTO!')
            ids = len(produtos['id_produto']) + 1
            produtos['id'].append(id_usuario)   
            produtos['id_produto'].append(ids)
            produtos['nome'].append(nome_produto.lower())
            produtos['quantidade'].append(int(input('Quantidade: ')))
            produtos['descricao'].append(input('Descrição: '))
            produtos['fornecedor'].append(None)##########
            produtos['alterado_por'].append(None)

            print('\nItem adicionado com sucesso!')

    else: 
        print('Você precisa está logado para acessar esta página.')

def alter_produto(usuario, usuarios, produtos, usuarios_logados):
    print('SESSÃO - ALTERAR PRODUTO!')

def remover_produto(usuario, usuarios, produtos, usuarios_logados):
    print('SESSÃO - REMOVER PRODUTO!')

# def entregar(usuario, id_usuario, produtos, entregas, relatorios): #Lembrar de criar relatórios
#     if usuario:
#         print('\nEnviar produto para um departamento:')
#         nome_produto = input('Nome do produto: ')
        
#         if nome_produto in produtos['nome']: 
#             for i, indice in enumerate((produtos['nome'])):
#                 if nome_produto == produtos['nome'][i]:
#                     print('\nID do produto: ', produtos['id_produto'][i], '\tQuantidade atual', produtos['quantidade'][i])
#                     id_prod = produtos['id_produto'][i]
#                     indice = produtos['nome'].index(nome_produto)
#                     while True:
#                         if produtos['quantidade'][indice] == 0:
#                             print('Produto fora de estoque. Não é possível enviar.')
#                             break
#                         else:
#                             qtd = int(input('Quantidade: '))
#                             if qtd > produtos['quantidade'][indice]:
#                                 print('Quantidade insuficiente. Disponível em estoque:', produtos['quantidade'][indice])
#                             else:
#                                 entregas['id'].append(id_usuario)
#                                 entregas['id_produto'].append(produtos['id_produto'][i])
#                                 destino = input('Departamento (1. Secretaria/2. Sala): ')

#                                 # entregas['dep_destino']['secretaria']['quantidade'] = 0
#                                 # entregas['dep_destino']['sala']['quantidade'] = 0
                                

#                                 if destino == '1':
#                                     if id_prod in entregas['id_produto']:
    #                                     entregas['dep_destino']['secretaria']['produto'].append(nome_produto)
    #                                     entregas['dep_destino']['secretaria']['quantidade'] += qtd
    #                                     produtos['quantidade'][i] -= qtd
#                                 elif destino == '2':
#                                     # if id_prod in entregas['id_produto']:
    #                                     entregas['dep_destino']['sala']['produto'].append(nome_produto)
    #                                     entregas['dep_destino']['sala']['quantidade'] += qtd
    #                                     produtos['quantidade'][i] -= qtd
#                                 else:
#                                     print('Destino inválido')
                                
#                                 entregas['data_entrega'].append(input('Data de entrega: '))
#                                 print(f'\n{nome_produto.title()}(s) entregue com sucesso!\n')
#                                 break
#                         break
#         else:
#             print('Produto não encontrado. Por favor, verifique se este produto está cadastrado.\n')


def inicio():
    return int(input('1. Fazer login\n2. Cadastrar-se\n3. Sair.\n=> '))

def main():

    usuarios = {
        'id': [],
        'nivel': [],
        'nome': [],
        'cpf': [],
        'senha': []
    }
   
    produtos = {
        'id': [],
        'id_produto': [],
        'nome': [],
        'quantidade': [],
        'descricao': [],
        'fornecedor': [],
        'alterado_por': []
    }

    entregas = {
        'id': [],
        'id_produto': [],
        'dep_destino': {
            'secretaria': {'produto': [], 'quantidade': []},
            'sala': {'produto':[], 'quantidade': []},
        },
        # 'quantidade': [],
        'data_entrega' : []
    }

    # departamentos

    relatorios = {
        'id': [],
        'nome': [],
        'prod_registrado': [],
        'prod_alterados': [],
        'data_alteracao': [],
        'data_remocao': []
        }

    usuarios_logados = set()
    while True:
        menu = inicio()
        if menu == 1:
            login(usuarios, produtos, usuarios_logados, entregas, relatorios)
        elif menu == 2:
            cadastro(usuarios, produtos, usuarios_logados)
        elif menu == 3:
            print('Saindo do almoxarifado...')
            print('Saiu.')
            break
        else:
            print('Inválido. Escolha umas das opções. ')

if __name__ == "__main__":
    main()