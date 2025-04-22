# controle_insumos_agro/main.py
from funcoes import *
from banco_oracle import *

menu = """
--- CONTROLE DE INSUMOS AGRÍCOLAS ---
1. Cadastrar novo insumo
2. Registrar entrada de estoque
3. Registrar saída de estoque
4. Listar insumos
5. Gerar relatório
6. Enviar dados ao banco Oracle
7. Sair
Digite a opção: """

while True:
    opcao = input(menu)

    if opcao == '1':
        cadastrar_insumo()
    elif opcao == '2':
        registrar_entrada()
    elif opcao == '3':
        registrar_saida()
    elif opcao == '4':
        listar_insumos()
    elif opcao == '5':
        gerar_relatorio_txt()
    elif opcao == '6':
        enviar_dados_oracle()
    elif opcao == '7':
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
