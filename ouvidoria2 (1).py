import os
from operacoesbd import *

tipos = ['Elogio', 'Reclamação', 'Sugestão', 'Denúncia']

def limpar():
    print("\033[2J\033[H", end="")

def voltarMenu():
    input('Pressione Enter para voltar.')
    limpar()

def quantidadeManifestacao(conexao):
    limpar()
    consulta = 'select count(*) from Manifestacoes;'
    manifestacoes = listarBancoDados(conexao, consulta)

    quantidadeManifestacao = manifestacoes[0][0]
    print('Atualmente temos', quantidadeManifestacao, 'manifestação(ões).')
    voltarMenu()

def removerManifestacao(conexao):
    limpar()

    codigoManifestacao = int(input("Digite o código da manifestação a ser removida: "))

    consultaVerificar = 'select * from Manifestacoes where codigo = %s'
    parametro = [codigoManifestacao]
    resultado = listarBancoDados(conexao, consultaVerificar, parametro)

    if len(resultado) == 0:
        print('Não existe manifestação para o código informado!')

    consulta = 'delete from Manifestacoes where codigo = %s;'
    valores = [codigoManifestacao]

    manifestacoesRemovidas = excluirBancoDados(conexao, consulta, valores)

    if manifestacoesRemovidas > 0:
        print('Manifestação removida com sucesso!')

    else:
        print('Tente novamente!')
    voltarMenu()

def pesquisarManifestacoesCodigo(conexao):
    limpar()

    codigoManifestacao = int(input('Digite o código da manifestação a ser pesquisada: '))

    consulta = 'select * from Manifestacoes where codigo = %s'
    dados = [codigoManifestacao]
    manifestacoes = listarBancoDados(conexao, consulta, dados)

    if len(manifestacoes) == 0:
        print('Nenhuma manifestação encontrada com esse código.')

    else:
        for item in manifestacoes:
            print('Código:', item[0], 'Descrição:', item[1], 'Autor:', item[2], 'Tipo:', item[3])
    voltarMenu()

def adicionarManifestacao(conexao):
    limpar()

    novaDescricao = input('Digite a descrição da manifestação: ')
    novoAutor = input('Digite o nome do autor: ')

    for i, item in enumerate(tipos, start=1):
        print(f'[{i}] {item}')
    tipoManifestacao = int(input('Digite o código referente ao tipo da manifestação: '))

    if tipoManifestacao < 1 or tipoManifestacao > len(tipos):
        print('Opção Inválida.')
    else:
        tipoManifestacao = tipos[tipoManifestacao - 1]

    consulta = 'insert into Manifestacoes (descricao, autor, tipo) values (%s, %s, %s);'
    dados = [novaDescricao, novoAutor, tipoManifestacao]
    codigoNovaManifestacoes = insertNoBancoDados(conexao, consulta, dados)

    print('Manifestação registrada com sucesso! O código é:', codigoNovaManifestacoes)
    voltarMenu()


def listarManifestacoes(conexao):
    limpar()
    for i, item in enumerate(tipos, start=1):
        print(f'[{i}] {item}')
    print(f'[{len(tipos) + 1}] Todos')

    tipo = int(input('Selecione uma opção: '))

    if tipo < 1 or tipo > len(tipos) + 1:
        print('Opção Inválida.')

    elif tipo == len(tipos) + 1:
        consulta = 'select * from Manifestacoes;'
        manifestacoes = listarBancoDados(conexao, consulta)

        if len(manifestacoes) == 0:
            print('Nenhuma manifestação a ser exibida.')

        else:
            for item in manifestacoes:
                print(item[0], '-', item[1], '- autor:', item[2], '-', item[3])

    else:
        tipo = tipos[tipo - 1]
        consulta = 'select * from Manifestacoes WHERE tipo = %s;'
        parametro = [tipo]
        manifestacoes = listarBancoDados(conexao, consulta, parametro)

        if len(manifestacoes) == 0:
            print('Nenhuma manifestação a ser exibida.')

        else:
            for item in manifestacoes:
                print(item[0], '-', item[1], '- autor:', item[2], '-', item[3])

    voltarMenu()
