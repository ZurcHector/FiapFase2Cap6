# controle_insumos_agro/banco_oracle.py
import cx_Oracle
import json
from funcoes import carregar_dados

# Configure aqui seus dados de conexão Oracle
USER = 'SYSTEM'
PASSWORD = 'DB280802'
DSN = 'localhost/XE'  # Exemplo para banco local com XE

# Enviar dados do JSON para tabela Oracle
def enviar_dados_oracle():
    dados = carregar_dados()
    try:
        conexao = cx_Oracle.connect(USER, PASSWORD, DSN)
        cursor = conexao.cursor()

        for item in dados:
            cursor.execute('''
                INSERT INTO INSUMOS (NOME, TIPO, QUANTIDADE, VALIDADE)
                VALUES (:1, :2, :3, TO_DATE(:4, 'DD/MM/YYYY'))
            ''', (item['nome'], item['tipo'], item['quantidade'], item['validade']))

        conexao.commit()
        print("Dados enviados ao banco Oracle com sucesso!")

    except Exception as e:
        print("Erro ao conectar/enviar para o banco:", e)

    finally:
        if 'conexao' in locals():
            conexao.close()
