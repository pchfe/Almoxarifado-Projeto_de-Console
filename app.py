
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


def login(usuarios, produtos, usuarios_logados):
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
                    print('\nLogin bem sucedido!\n')
                    nivel = usuarios['nivel'][i] #extrair o nivel de permissão
                    nome = usuarios['nome'][i] #extrarir o nome do usuario logado
                    filtro = filtrar_nivel(nivel, usuarios)
                    almoxarifado(usuario, filtro, nome, usuarios, produtos, usuarios_logados)
    else:
        print('\nOps! Parece que este CPF não está cadastrado. Tente novamente.\n ')

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios['cpf'] if usuario == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def filtrar_nivel(nivel, usuarios):
    nivel_filtrado = [filtro for filtro in usuarios['nivel'] if filtro == nivel]
    return nivel_filtrado[0] if nivel_filtrado else None

def almoxarifado(usuario, filtro, nome, usuarios, produtos, usuarios_logados):
    filtro = filtrar_nivel(filtro, usuarios)
    while True:
        print_menu(usuario, filtro, nome, usuarios)
        if usuario:
            if filtro == 1:
                menu = int(input('=> '))
                if menu == 1:
                    add_produto(usuario, usuarios, produtos, usuarios_logados)
                elif menu == 2:
                    print('\nsaindo....')
                else:
                    print('\nOps! Você não tem permissão para acessar esta sessão.\n')
                # nivel_1(usuario, usuarios, produtos)
            elif filtro == 2:
                menu = int(input('=> '))
                if menu == 1:
                    add_produto(usuario, usuarios, produtos, usuarios_logados)
                elif menu == 2:
                    alter_produto(usuario, usuarios, produtos, usuarios_logados)
                # nivel_2(usuario, usuarios, produtos)
                elif menu == 3:
                    print('removendo produto...')##
                else:
                    print('\nOps! Você não tem permissão para acessar esta sessão.\n')
            else:
                print('Ops! Você não tem permissão suficiente para acessar o almoxarifado.\n')
        else:
            print('\nErro! Faça login para acessar esta página.\n')

def print_menu(usuario, filtro, nome, usuarios):
    print(f'\nOlá, {nome}! - Bem vindo ao Almoxarifado:')
    if filtro == 1:
        print('1. Adicionar produto')
        print('2. Sair do almoxarifado')
    elif filtro == 2:
        print('1. Adicionar produto')
        print('2. Alterar produto')
        print('3. Remover produto')
        print('4. Sair do almoxarifado')
    else:
        print('Nível de acesso inválido.')




def add_produto(usuario, usuarios, produtos, usuarios_logados):
    print('SESSÃO - ADICIONAR PRODUTO!')

def alter_produto(usuario, usuarios, produtos, usuarios_logados):
    print('SESSÃO - ALTERAR PRODUTO!')

def remover_produto(usuario, usuarios, produtos, usuarios_logados):
    print('SESSÃO - REMOVER PRODUTO!')


def inicio():
    return int(input('1. Fazer login\n2. Cadastrar-se\n3. Sair.\n=> '))

def main():
    usuarios = {'id': [], 'nivel': [], 'nome': [], 'cpf': [], 'senha': []}
    produtos = {'id': [], 'nome': [], 'quantidade': [], 'descricao': []} #adicionar id/nome de quem fez alteração no produto 
    usuarios_logados = set()
    while True:
        menu = inicio()
        if menu == 1:
            login(usuarios, produtos, usuarios_logados)
        elif menu == 2:
            cadastro(usuarios, produtos, usuarios_logados)
        elif menu == 3:
            break
        else:
            print('Inválido. Escolha umas das opções. ')

if __name__ == "__main__":
    main()