from operacoesbd import *
from ouvidoria2 import *
from operacoesbd import *

conexao = criarConexao('localhost','root','1234','projeto_ouvidoria')

opcao = -1
manifestacoes = []

while opcao != 6:
    print('\n   MENU DE MANIFESTAÇÕES')
    print('1) Listar Manifestações')
    print('2) Registrar Manifestação')
    print('3) Procurar Manifestação pelo código')
    print('4) Remover Manifestação')
    print('5) Quantidade de Manifestações')
    print('6) Sair')

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        listarManifestacoes(conexao)

    elif opcao == 2:
        adicionarManifestacao(conexao)

    elif opcao == 3:
        pesquisarManifestacoesCodigo(conexao)

    elif opcao == 4:
        removerManifestacao(conexao)

    elif opcao == 5:
        quantidadeManifestacao(conexao)

    elif opcao != 6:
        print('Opção inválida!')

print('Obrigado por usar o App da Ouvidoria!')

encerrarConexao(conexao)