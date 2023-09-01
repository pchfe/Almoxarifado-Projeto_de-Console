def inicio():
    return int(input('1. Fazer login\n2. Cadastrar-se\n==> '))


def almoxarifado(usuario, id_, usuarios_logados, usuarios, produtos, ids):
    if usuario and id_ in usuarios_logados: 
        print('Acessando almoxarifado cadastro!')
        menu_amoxarifado(usuario, usuarios, id_, usuarios_logados, produtos, ids)
        # almoxarifado_cadastro(usuarios, usuarios_logados, produtos)
    else:
        return print('Acesso negado!')
    
    
def menu_amoxarifado(usuario, usuarios, id_, usuarios_logados, produtos, ids):
    while True:
        menu = int(input('\n1. Acessar estoque dos produtos\n2. Consultar por produto\n3. Enviar produto para um Departamento\n4. Alterar produto\n5. Adicionar produto\n6. Remover produto\n7. Sair do almoxarifado\n==> '))
        if menu == 1:
            exibir_produtos_geral(produtos) #######
        elif menu == 2:
            exibir_produtos_consulta(usuarios, produtos)
        elif menu == 3:
            pass
        elif menu == 4:
            alterar_produto(usuario, usuarios, id_, usuarios_logados, produtos, ids)
        elif menu == 5:
            adicionar_produto(usuario, usuarios, id_, usuarios_logados, produtos, ids)
        elif menu == 6:
            print('.....')
        elif menu == 7:
            return fazer_logout(usuario, id_, usuarios, usuarios_logados)


def adicionar_produto(usuario, usuarios, id_, usuarios_logados, produtos, ids):
    # adc_produto = id_
    # if usuario in usuarios_logados and id_ in ids:
    if usuario and id_ in usuarios_logados:
        print('SEU ID: ', id_) #Apenas para testar se o id está sendo chamado corretamente
        produtos['nome'].append(input('Nome do produto: '))
        produtos['tipo'].append(input('Tipo: '))
        n = None
        produtos['descricao'].append(n)
        produtos['quem_recebe'].append(n)
        produtos['quantidade'].append(n)
        # if adc_produto == id_:
        #     # produtos['ult_alteracao'].append(id_) # Registra o último usuário a fazer alteração no produto
        produtos['ult_alteracao'].append('Sem alteração')
        # else:
        produtos['id_criador'].append(id_) #Registra quem criou o produto
        
    else:
        print('Você deve logar para adicionar um produto.')


def alterar_produto(usuario, usuarios, id_, usuarios_logados, produtos, ids):
    print('Alteração de quantidade de produtos:\n')
    nome = input('Nome do produto: ')
    tipo = input('Tipo: ')
    if tipo in produtos['tipo']: #Verifica se existe produto com mesmo tipo cadastrado
        for i, alter in enumerate((produtos['nome'])):
            if nome == produtos['nome'][i] and tipo == produtos['tipo'][i]: # Se o tipo existe, verifica se o nome do produto é igual
                # if usuario in usuarios_logados and id_ in ids:
                print('Quantidade atual: ', produtos['quantidade'])
                produtos['quantidade'][i] = int(input('Nova quantidade: '))
                produtos['descricao'][i] = None
                produtos['quem_recebe'][i] = None
                # produtos['id_criador'][i] = id_
                produtos['ult_alteracao'][i] = id_  # Registra o usuário que fez a alteração
                print('\nQuantidade alterado com sucesso!\n')
            else:
                print('Acesso negado!')
            break

        else:
            print('Produdo não encontrado.')

def fazer_logout(usuario, id_, usuarios, usuarios_logados):
    if usuario in usuarios_logados:
        # usuarios_logados.remove(id_)
        usuarios_logados.remove(usuario)
        print('Logout bem sucedido!\n')
        return
    else:
        print('Você não está logado')


def login(usuarios, usuarios_logados, produtos, ids):
    cpf = int(input('Informe seu CPF (apenas números): '))
    senha = input('Digite a sua senha: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario and senha in usuarios['senha']:
        if usuario in usuarios_logados:
            print('Você já está logado.')
        else:
            usuarios_logados.add(usuario)
            for i, meuid in enumerate(usuarios['id']):
                id_ = meuid
                print('Login bem-sucedido!')
                # usuarios_logados.add(id_)
                ids.add(id_)
                print('ID logado: ', id_, '\nmeuid: ', meuid) ###Apenas para indicar que está funcionando o id
                almoxarifado(usuario, id_, usuarios_logados, usuarios, produtos, ids)
    else:
        print('Usuário não encontrado. Tente novamente.')



def cadastro(usuarios, usuarios_logados, produtos, ids):
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
    
    id_ = len(usuarios['id']) + 1
    usuarios['id'].append(id_)
    ids.add(id_)####
    usuarios['nome'].append(nome)
    usuarios['cpf'].append(cpf)
    usuarios['senha'].append(input('Digite a sua senha (6 caracteres, no mínimo.): '))
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
        print(f'\nProduto {i+1}: ', produtos['nome'][i], '\nDescrição: ', produtos['descricao'][i], '\nTipo: ', produtos['tipo'][i], '\nQuantidade: ', produtos['quantidade'][i], '\nQuem recebe: ', produtos['quem_recebe'][i], '\nAlterado por: ', produtos['ult_alteracao'][i], '\nCriado por: ', produtos['id_criador'][i], '\n')



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
    ids = set() ###
    produtos = {'nome': [], 'descricao': [], 'tipo': [], 'quantidade': [], 'quem_recebe': [], 'ult_alteracao': [], 'id_criador': []} #tipo = camisa, garrafa, etc

    while True:

        menu = inicio()
        if menu == 1:
            login(usuarios, usuarios_logados, produtos, ids)
        elif menu == 2:
            cadastro(usuarios, usuarios_logados, produtos, ids)
        elif menu == 3:
            almoxarifado(usuarios, usuarios_logados, produtos, ids)
        elif menu == 4:
            exibir_produtos_geral(produtos)
        else:
            print('Inválido.')

if __name__ == "__main__":
    main()
