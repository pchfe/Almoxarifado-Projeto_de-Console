from produtos.cadastro import almoxarifado_cadastro
from filtros.filtro import exibir_produtos_geral, exibir_produtos_consulta

def inicio():
    return int(input('1. Fazer login\n2. Cadastrar-se\n==> '))

def almoxarifado(usuario, usuarios_logados, usuarios, produtos):
    if usuario in usuarios_logados: 
        print('Acessando almoxarifado cadastro!')
        menu_amoxarifado(usuarios, produtos)
        # almoxarifado_cadastro(usuarios, usuarios_logados, produtos)
    else:
        return print('Acesso negado!')
    
def menu_amoxarifado(usuarios, produtos):
    while True:
        menu = int(input('\n1. Acessar estoque dos produtos\n2. Consultar por produto\n3. Enviar produto para um Departamento\n4. Alterar produto\n5. Remover produto\n==> '))
        if menu == 1:
            exibir_produtos_geral(usuarios, produtos)
        elif menu == 2:
            exibir_produtos_consulta(usuarios, produtos)