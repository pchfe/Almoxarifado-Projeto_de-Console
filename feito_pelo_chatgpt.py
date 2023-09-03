######
######
    # CRIADO COM CHATGPT BASEADO NO MEU CÓDIGO, 
    # IMPLEMENTANDO O BANCO DE DADOS MYSQL #
#####
#####
import mysql.connector


def almoxarifado(usuario_id, cursor, conn):
    query = "SELECT nome, nivel_permissao FROM usuarios WHERE id = %s"
    cursor.execute(query, (usuario_id,))
    result = cursor.fetchone()
    
    if result:
        nome, acesso = result
        print('\n===== Almoxarifado SENAI =====\n')
        if acesso == 1:
            menu_amoxarifado(usuario_id, nome, cursor, conn)
        elif acesso == 2:
            menu_almoxarifado_nivel_2(usuario_id, nome, cursor, conn)
        else:
            print('Erro.')
    else:
        print('Erro ao recuperar informações do usuário.')

    
def menu_amoxarifado(usuario_id, nome, cursor, conn):
    while True:
        menu = int(input('\n1. Acessar estoque dos produtos\n2. Consultar por produto\n3. Enviar produto para um Departamento\n4. Sair do almoxarifado\n==> '))
        if menu == 1:
            exibir_produtos_geral(cursor)
        elif menu == 2:
            exibir_produtos_consulta(cursor)
        elif menu == 3:
            print('Enviando produto para um departamento...')  # Implemente esta funcionalidade
        elif menu == 4:
            return

def menu_almoxarifado_nivel_2(usuario_id, nome, cursor, conn):
    print(f'Olá, {nome}')
    while True:
        menu = int(input('\n1. Acessar estoque dos produtos\n2. Consultar por produto\n3. Enviar produto para um Departamento\n4. Alterar produto\n5. Adicionar produto\n6. Remover produto\n7. Sair do almoxarifado\n==> '))
        if menu == 1:
            exibir_produtos_geral(cursor)
        elif menu == 2:
            exibir_produtos_consulta(cursor)
        elif menu == 3:
            print('Enviando um produto para um departamento...')  # Implemente esta funcionalidade
        elif menu == 4:
            alterar_produto(cursor, conn)
        elif menu == 5:
            adicionar_produto(cursor, conn)
        elif menu == 6:
            print('Removendo um produto...')  # Implemente esta funcionalidade
        elif menu == 7:
            return

def adicionar_produto(cursor, conn):
    nome = input('Nome do produto: ')
    tipo = input('Tipo: ')
    
    insert_query = "INSERT INTO produtos (nome, tipo) VALUES (%s, %s)"
    produto_data = (nome, tipo)

    try:
        cursor.execute(insert_query, produto_data)
        conn.commit()
        print('Produto adicionado com sucesso!')
    except mysql.connector.Error as err:
        print(f'Erro ao adicionar produto: {err}')

def alterar_produto(cursor, conn):
    nome = input('Nome do produto: ')
    tipo = input('Tipo: ')
    quantidade = int(input('Nova quantidade: '))
    
    update_query = "UPDATE produtos SET quantidade = %s WHERE nome = %s AND tipo = %s"
    produto_data = (quantidade, nome, tipo)
    
    try:
        cursor.execute(update_query, produto_data)
        conn.commit()
        print('Quantidade alterada com sucesso!')
    except mysql.connector.Error as err:
        print(f'Erro ao alterar quantidade do produto: {err}')

def exibir_produtos_geral(cursor):
    query = "SELECT nome, tipo, quantidade FROM produtos"
    cursor.execute(query)
    result = cursor.fetchall()

    print('=' * 20)
    for produto in result:
        nome, tipo, quantidade = produto
        print(f'Produto: {nome}')
        print(f'Tipo: {tipo}')
        print(f'Quantidade: {quantidade}')
        print('=' * 20)

def exibir_produtos_consulta(cursor):
    nome = input('Qual produto está buscando?\n==> ')
    tipo = input('Qual o tipo do produto?\n==> ')

    query = "SELECT nome, tipo, quantidade FROM produtos WHERE nome = %s AND tipo = %s"
    cursor.execute(query, (nome, tipo))
    result = cursor.fetchall()

    if result:
        for produto in result:
            nome, tipo, quantidade = produto
            print(f'Produto: {nome}, Tipo: {tipo}, Quantidade: {quantidade}')
    else:
        print('Produto não encontrado.')


def login(cursor, conn):
    cpf = input('Informe seu CPF (apenas números): ')
    senha = input('Digite a sua senha: ')
    
    query = "SELECT id, nome FROM usuarios WHERE cpf = %s AND senha = %s"
    cursor.execute(query, (cpf, senha))
    result = cursor.fetchone()

    if result:
        usuario_id, nome = result
        # print(f'Login bem-sucedido!\nBem-vindo, {nome}!')
        print(f'Login bem-sucedido!\n')
        return usuario_id
    else:
        print('Usuário não encontrado ou senha incorreta. Tente novamente.')
        return None


def logout(usuario_id):
    print('Logout bem-sucedido!')

def cadastro(cursor, conn):
    nome = input('Digite o seu nome: ')
    cpf = int(input('Informe o seu CPF (apenas números): '))
    
    if verificar_cpf_existente(cursor, cpf):
        print('CPF já cadastrado. Não é possível criar outro cadastro com o mesmo CPF.')
        return
    
    senha = input('Digite a sua senha (6 caracteres, no mínimo.): ')

    print('Escolha a instituição à qual você faz parte:')
    print('1. Dendezeiros')
    print('2. Cimatec')
    instituicao = input('==> ')

    if instituicao not in ('1', '2'):
        print('Opção inválida.')
        return

    query = "INSERT INTO usuarios (nome, cpf, instituicao, senha, nivel_permissao) VALUES (%s, %s, %s, %s, %s)"
    usuario_data = (nome, cpf, 'Dendezeiros' if instituicao == '1' else 'Cimatec', senha, 2)

    try:
        cursor.execute(query, usuario_data)
        conn.commit()
        print('Cadastro realizado com sucesso!')
    except mysql.connector.Error as err:
        print(f'Erro ao cadastrar: {err}')

def verificar_cpf_existente(cursor, cpf):
    query = "SELECT id FROM usuarios WHERE cpf = %s"
    cursor.execute(query, (cpf,))
    result = cursor.fetchone()
    return result is not None

def verificar_login(cpf, senha, cursor):
    query = "SELECT id FROM usuarios WHERE cpf = %s AND senha = %s"
    cursor.execute(query, (cpf, senha))
    result = cursor.fetchone()
    return result[0] if result else None

def inicio():
    return int(input('1. Fazer login\n2. Cadastrar-se\n==> '))


def main():

    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Windowscodec1!",
    database="almoxarifado"
    )
    cursor = conn.cursor()

    usuario_id = None

    while True:
        menu = inicio()
        if menu == 1:
            usuario_id = login(cursor, conn)
            if usuario_id is not None:
                almoxarifado(usuario_id, cursor, conn)
        elif menu == 2:
            cadastro(cursor, conn)
        elif menu == 3:
            if usuario_id is not None:
                logout(usuario_id)
                usuario_id = None
            else:
                print('Você não está logado.')
        else:
            print('Opção inválida.')

if __name__ == "__main__":
    main()

######
######
    # CRIADO COM CHATGPT BASEADO NO MEU CÓDIGO, 
    # IMPLEMENTANDO O BANCO DE DADOS MYSQL #
#####
#####