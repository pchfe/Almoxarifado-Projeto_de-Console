def inicio():
    return int(input('1. Fazer login\n2. Cadastrar-se\n==> '))


def almoxarifado(usuario, usuarios_logados, usuarios, produtos):
    if usuario in usuarios_logados: 
        print('Acessando almoxarifado cadastro!')
        menu_amoxarifado(usuario, usuarios, usuarios_logados, produtos)
        # almoxarifado_cadastro(usuarios, usuarios_logados, produtos)
    else:
        return print('Acesso negado!')
    
    
def menu_amoxarifado(usuario, usuarios, usuarios_logados, produtos):
    while True:
        menu = int(input('\n1. Acessar estoque dos produtos\n2. Consultar por produto\n3. Enviar produto para um Departamento\n4. Alterar produto\n5. Adicionar produto\n6. Remover produto\n7. Sair do almoxarifado\n==> '))
        if menu == 1:
            exibir_produtos_geral(produtos) #######
        elif menu == 2:
            exibir_produtos_consulta(usuarios, produtos)
        elif menu == 3:
            pass
        elif menu == 4:
            alterar_produto(usuario, usuarios, usuarios_logados, produtos)
        elif menu == 5:
            adicionar_produto(usuario, usuarios, usuarios_logados, produtos)
        elif menu == 6:
            print('.....')
        elif menu == 7:
            # return fazer_logout(usuario, meuid, usuarios, usuarios_logados)
            fazer_logout(usuario, usuarios_logados)
            break


def adicionar_produto(usuario, cpf, usuarios, usuarios_logados, produtos):
    # user = filtrar_usuario(cpf, usuarios)
    # usuario = filtrar_usuario(cpf, usuarios)
    if usuario in usuarios_logados:
        md = usuario['id']
        # for i, j in enumerate(usuarios['cpf']):
        #     if j == cpf:
        #         print('Id login: ', usuarios['id'][i])
        #         print('i: ',i, 'j: ', j)
        #         md = usuarios['id'][i]
        
        print('SEU ID: ', md)
        produtos['nome'].append(input('Nome do produto: '))
        produtos['tipo'].append(input('Tipo: '))
        produtos['descricao'].append(input('Descrição: '))
        produtos['quem_recebe'].append(input('Quem recebe? '))
        produtos['quantidade'].append(input('Quantidade: '))
        produtos['id_produto'].append(md)
    else:
        print('Você deve logar para adicionar um produto.')


def alterar_produto(usuario, usuarios, usuarios_logados, produtos):
    print('Alteração de quantidade de produtos:\n')
    nome = input('Nome do produto: ')
    tipo = input('Tipo: ')
    # if tipo in produtos['tipo']: #### 
    for i, alter in enumerate((produtos['nome'])):
        if nome == produtos['nome'][i] and tipo == produtos['tipo'][i]:
            print('Quantidade atual: ', produtos['quantidade'])
            nova_quantidade = int(input('Nova quantidade: '))
            produtos['quantidade'][i] = nova_quantidade
            produtos['id_produto'][i] = usuario['id']
            print('\nQuantidade alterado com sucesso!\n')
            break
    else:
        print('Produto não encontrado.\n')


def fazer_logout(usuario, usuarios_logados):
    if usuario in usuarios_logados:
        usuarios_logados.remove(usuario)
        # usuarios_logados.remove(meuid)
        print('Logout bem sucedido!\n')
        return
    else:
        print('Você não está logado')


def login(usuarios, usuarios_logados, produtos):
    cpf = int(input('Informe seu CPF (apenas números): '))
    senha = input('Digite a sua senha: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario and senha in usuarios['senha']:
        for i, j in enumerate(usuarios['cpf']):
            if j == cpf:
                print('Id login: ', usuarios['id'][i])
                print('i: ',i, 'j: ', j)
                if usuario in usuarios_logados:
                    print('Você já está logado.')
                    # return usuario
        else:
            usuarios_logados.add(usuario)
            meuid = usuarios['id'][i]
            almoxarifado(usuario, usuarios_logados, usuarios, produtos)
            # for i, myid in enumerate(usuarios['id']):
            #     meuid = myid
            #     print('Login bem-sucedido!')
            #     # usuarios_logados.add(meuid)
            #     print('ID logado: ', meuid, '\nmeuid: ', myid)
            #     almoxarifado(usuario, meuid, usuarios_logados, usuarios, produtos)
    else:
        print('Usuário não encontrado. Tente novamente.')



def cadastro(usuarios, usuarios_logados, produtos):
    nome = input('Digite o seu nome: ')
    cpf = int(input('Informe o seu CPF (apenas números): '))
    
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        return print('@@@ Erro! Usuário com este CPF já está cadastrado. @@@')

    instituicao = input('Escolha a instituiçâo a qual você faz parte: | 1. Dendezeiros\t2. Cimatec |\n==> ')
    inst = filtrar_instituicao(instituicao, usuarios) 
    if inst is not None:
        usuarios['instituicao'].append('Dendezeiros' if instituicao == '1' else 'Cimatec')
    else:
        print('@@@ Ops! Instituicao não encontrada. @@@\n')
    
    meuid = len(usuarios['id']) + 1
    usuarios['id'].append(meuid)
    usuarios['nome'].append(nome)
    usuarios['cpf'].append(cpf)
    usuarios['senha'].append(input('Digite a sua senha (6 caracteres, no mínimo.): '))
    print('id cadastro:', meuid)
    print('=== Obrigado por se cadastrar! ===')


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
def exibir_produtos_geral(produtos):
    # produtos = {'nome': [], 'descricao': [], 'tipo': [['Camiseta', 'Garrafinha']], 'quantidade': [], 'quem_recebe': []}
    for i, geral in enumerate(produtos['nome']):
        # print(f'\nProduto {i+1}: ', produtos['nome'][i], '\nDescrição: ', produtos['descricao'][i], '\nTipo: ', produtos['tipo'][i], '\nQuantidade: ', produtos['quantidade'][i], '\n')
        print(f'\nProduto {i+1}: ', produtos['nome'][i], '\nDescrição: ', produtos['descricao'][i], '\nTipo: ', produtos['tipo'][i], '\nQuantidade: ', produtos['quantidade'][i], '\nQuem recebe: ', produtos['quem_recebe'][i], '\nAlterado por: ', produtos['id_produto'][i], '\n')



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



def main():
    usuarios = {'id': [], 'nome': [], 'cpf': [], 'instituicao': [], 'senha': []}
    usuarios_logados = set()
    produtos = {'nome': [], 'descricao': [], 'tipo': [], 'quantidade': [], 'quem_recebe': [], 'id_produto': []} #tipo = camisa, garrafa, etc

    while True:

        menu = inicio()
        if menu == 1:
            login(usuarios, usuarios_logados, produtos)
            almoxarifado(usuarios_logados, usuarios, produtos)
        elif menu == 2:
            cadastro(usuarios, usuarios_logados, produtos)
        elif menu == 3:
            almoxarifado(usuarios, usuarios_logados, produtos)
        elif menu == 4:
            exibir_produtos_geral(produtos)
        else:
            print('Inválido.')

if __name__ == "__main__":
    main()
