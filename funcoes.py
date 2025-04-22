# controle_insumos_agro/funcoes.py
import json
from datetime import datetime

CAMINHO_ARQUIVO = 'dados.json'

# Função auxiliar para carregar dados
def carregar_dados():
    try:
        with open(CAMINHO_ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Função auxiliar para salvar dados
def salvar_dados(dados):
    with open(CAMINHO_ARQUIVO, 'w') as f:
        json.dump(dados, f, indent=4)

# Cadastro de novo insumo
def cadastrar_insumo():
    nome = input("Nome do insumo: ")
    tipo = input("Tipo (fertilizante, defensivo, semente): ")
    quantidade = int(input("Quantidade inicial: "))
    validade = input("Validade (dd/mm/aaaa): ")

    dados = carregar_dados()
    dados.append({
        "nome": nome,
        "tipo": tipo,
        "quantidade": quantidade,
        "validade": validade
    })
    salvar_dados(dados)
    print("Insumo cadastrado com sucesso!")

# Registro de entrada
def registrar_entrada():
    nome = input("Nome do insumo: ")
    qtd = int(input("Quantidade a adicionar: "))
    dados = carregar_dados()
    for item in dados:
        if item['nome'].lower() == nome.lower():
            item['quantidade'] += qtd
            salvar_dados(dados)
            print("Entrada registrada.")
            return
    print("Insumo não encontrado.")

# Registro de saída
def registrar_saida():
    nome = input("Nome do insumo: ")
    qtd = int(input("Quantidade a remover: "))
    dados = carregar_dados()
    for item in dados:
        if item['nome'].lower() == nome.lower():
            if item['quantidade'] >= qtd:
                item['quantidade'] -= qtd
                salvar_dados(dados)
                print("Saída registrada.")
            else:
                print("Quantidade insuficiente em estoque.")
            return
    print("Insumo não encontrado.")

# Listar todos os insumos
def listar_insumos():
    dados = carregar_dados()
    print("\n--- LISTA DE INSUMOS ---")
    for item in dados:
        print(f"Nome: {item['nome']} | Tipo: {item['tipo']} | Qtd: {item['quantidade']} | Validade: {item['validade']}")

# Gerar relatório .txt
def gerar_relatorio_txt():
    dados = carregar_dados()
    with open('relatorio.txt', 'w') as f:
        f.write("RELATÓRIO DE INSUMOS\n")
        f.write(f"Gerado em: {datetime.now()}\n\n")
        for item in dados:
            f.write(f"Nome: {item['nome']} | Tipo: {item['tipo']} | Qtd: {item['quantidade']} | Validade: {item['validade']}\n")
    print("Relatório gerado em 'relatorio.txt'.")
