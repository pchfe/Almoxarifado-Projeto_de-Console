#Niveis de permissão:
    # Nivel 1 - Pode visualizar e enviar produtos
    # Nivel 2 - Pode visualizar, adicionar, alterar, remover e enviar
    # Nivel 3 - Pode remover usuários e alterar nivel de permissão, além de todas as outras funcionalidades mensionadas.


def cadastro(usuarios, usuarios_logados, produtos):
    print('\nSessão | Cadastrar |\n')
    cpf = int(input('Informe o CPF: '))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('\nUm usuário com este CPF já está cadastrado.\n')
    else:
        while True:
            nome = input('Informe o seu nome: ')
            senha = input('Informe a sua senha (minimo de 6 caracteres): ')
            if senha is not None and len(senha) >= 6 and len(nome) > 0:
                usuarios['id_permissao'].append(2) #Nivel de permissão
                usuarios['nome'].append(nome)
                usuarios['senha'].append(senha)
                usuarios['cpf'].append(cpf)
                print('\nUsuário cadastrado com sucesso! - Faça login agora para entrar\n')
                login(usuarios, usuarios_logados, produtos)
                break
            else:
                print('Nome ou senha inválida.')


def login(usuarios, usuarios_logados, produtos):
    print('Sessão | Login |\n')
    cpf = int(input('Informe o seu CPF: '))
    senha = input('Informe a sua Senha: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario and senha in usuarios['senha']:
        # nome = nome_usuario(cpf, usuarios)
        if usuario in usuarios_logados:
            print('\nVocê já está logado.\n')
        else:
            usuarios_logados.add(usuario)

            print('\nLogin bem sucedido!\n\n')
            if cpf in usuarios['cpf']:
                user = usuarios['cpf'].index(cpf)
                nome = usuarios['nome'][user]
                userId = usuarios['id_permissao'][user]
            tela_inicio(usuario, usuarios_logados, userId, nome, usuarios, produtos)
    else:
        print('\nErro! CPF ou senha inválidos. Tente novamente.\n')

def fazer_logout(usuario, usuarios, usuarios_logados):
    if usuario in usuarios_logados:
        usuarios_logados.remove(usuario)
        print('\nVocê saiu.\n')
        return
    else:
        print('Você não está logado')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios['cpf'] if usuario == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def adicionar_produto(usuario, usuarios, produtos):
    print('\nSessão - Adicionar produto') # Implementar mais tarde

def enviar_produto(usuario, usuarios, produtos):
    print('\nSessão - Enviar produto') # Implementar mais tarde

def alterar_produto(usuario, usuarios, produtos):
    print('\nSessão - Alterar produto') # Implementar mais tarde

def remover_produto(usuario, usuarios, produtos):
    print('\nSessão - Remover produto') # Implementar mais tarde

def consultar_produto(usuario, usuarios, produtos):
    print('\nSessão - Visualizar produto') # Implementar mais tarde

def remover_usuario(usuario, usuarios, produtos):
    print('\nSessão - Remover usuários')

def print_menu(userId, nome):
    print(f'\nOlá, {nome}! | Bem vindo(a) ao Almoxarifado Senai |\n')
    if userId == 1:
        print(' 1. Adicionar produto')
        print(' 2. Enviar para um departamento')
        print(' 3. Consultar estoque')
        print(' 4. Sair do almoxarifado')
    elif userId == 2:
        print(' 1. Adicionar produto')
        print(' 2. Alterar produto')
        print(' 3. Remover produto')
        print(' 4. Enviar para um departamento')
        print(' 5. Consultar o estoque')
        print(' 6. Sair do almoxarifado')
    elif userId == 3:
        print(' 1. Adicionar produto')
        print(' 2. Alterar produto')
        print(' 3. Remover produto')
        print(' 4. Enviar para um departamento')
        print(' 5. Consultar o estoque')
        print(' 6. Remover usuários')
        print(' 7. Sair do almoxarifado')
    else:
        print('\nVocê não tem permissão para acessar o almoxarifado.\n')


def tela_inicio(usuario, usuarios_logados, userId, nome, usuarios, produtos):
    if usuario:
        while True: 
            print_menu(userId, nome)
            menu = int(input('=> '))
            if userId == 1:
                if menu == 1:
                    adicionar_produto(usuario, usuarios, produtos)
                elif menu == 2:
                    enviar_produto(usuario, usuarios, produtos)
                elif menu == 3:
                    consultar_produto(usuario, usuarios, produtos)
                elif menu == 4:
                    fazer_logout(usuario, usuarios, usuarios_logados)
                    break

            elif userId == 2:
                if menu == 1:
                    adicionar_produto(usuario, usuarios, produtos)
                elif menu == 2:
                    alterar_produto(usuario, usuarios, produtos)
                elif menu == 3:
                    remover_produto(usuario, usuarios, produtos)
                elif menu == 4:
                    enviar_produto(usuario, usuarios, produtos)
                elif menu == 5:
                    consultar_produto(usuario, usuarios, produtos)
                elif menu == 6:
                    fazer_logout(usuario, usuarios, usuarios_logados)
                    break
            
            elif userId == 3:
                if menu == 1:
                    adicionar_produto(usuario, usuarios, produtos)
                elif menu == 2:
                    alterar_produto(usuario, usuarios, produtos)
                elif menu == 3:
                    remover_produto(usuario, usuarios, produtos)
                elif menu == 4:
                    enviar_produto(usuario, usuarios, produtos)
                elif menu == 5:
                    consultar_produto(usuario, usuarios, produtos)
                elif menu == 6:
                    remover_usuario(usuario, usuarios, produtos)
                elif menu == 7:
                    fazer_logout(usuario, usuarios, usuarios_logados)
                    break
    else:
        print('\nErro! Faça login para continuar.\n')


def inicio():
    return int(input('1. Fazer Login\n2. Cadastro\n3. Sair\n> '))

def main():
    usuarios = {
        'id_permissao': [],    
        'nome': [],
        'cpf': [],
        'senha': []
    }

    usuarios_logados = set()

    produtos = {
        'nome': [],
        'valor': [],
        'descricao': []
    }

    while True:
        menu = inicio()
        if menu == 1:
            login(usuarios, usuarios_logados, produtos)
        elif menu == 2:
            cadastro(usuarios, usuarios_logados, produtos)
        elif menu == 3:
            print('\nSaindo...\nSaiu.\n')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
  main()