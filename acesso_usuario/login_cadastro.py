from filtros.filtro import filtrar_usuario, filtrar_instituicao
from tela_inicio.inicio import almoxarifado


def login(usuarios, usuarios_logados, produtos):
    cpf = int(input('Informe seu CPF (apenas números): '))
    senha = input('Digite a sua senha: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario and senha in usuarios['senha']:
        if usuario in usuarios_logados:
            print('Você já está logado.')
        else:
            print('Login bem-sucedido!')
            usuarios_logados.add(usuario)
            almoxarifado(usuario, usuarios_logados, usuarios, produtos)
    else:
        print('Usuário não encontrado. Tente novamente.')


def cadastro(usuarios, usuarios_logados, produtos):
    nome = input('Digite o seu nome: ')
    cpf = int(input('Informe o seu CPF (apenas números): '))
    
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        return print('@@@ Erro! Usuário com este CPF já está cadastrado. @@@')

    instituicao = input('Ecolha a instituicao a qual você faz parte: | 1. Dendezeiros\t2. Cimatec |\n==> ')
    inst = filtrar_instituicao(instituicao, usuarios) 
    if inst is not None:
        usuarios['instituicao'].append('Dendezeiros' if instituicao == '1' else 'Cimatec')
    else:
        print('@@@ Ops! Instituicao não encontrada. @@@\n')
    
    usuarios['nome'].append(nome)
    usuarios['cpf'].append(cpf)
    usuarios['senha'].append(input('Digite a sua senha (6 caracteres, no mínimo.): '))
    print('=== Obrigado por se cadastrar! ===')
