from acesso_usuario.login_cadastro import login, cadastro
from filtros.filtro import filtrar_usuario, filtrar_instituicao, filtrar_produto_recebe, filtrar_produto_tipo, exibir_produtos_geral, exibir_produtos_consulta
from tela_inicio.inicio import inicio, almoxarifado

### Função principal
def main():
    usuarios = {'nome': [], 'cpf': [], 'instituicao': [], 'senha': []}
    usuarios_logados = set()
    produtos = {'nome': ['Camiseta senai'], 'descricao': ['Se trata de uma camiseta'], 'tipo': ['Camiseta'], 'quantidade': [25], 'quem_recebe': ['alunos']} #tipo = camisa, garrafa, etc

    while True:

        menu = inicio()
        if menu == 1:
            login(usuarios, usuarios_logados, produtos)
        elif menu == 2:
            cadastro(usuarios, usuarios_logados, produtos)
        elif menu == 3:
            almoxarifado(usuarios, usuarios_logados, produtos)
        elif menu == 4:
            login(usuarios, usuarios_logados, produtos)
        else:
            print('Inválido.')

if __name__ == "__main__":
    main()
