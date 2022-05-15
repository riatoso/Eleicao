# SISTEMA DE CLEINTES
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Mai-2022
# version ='1.0'
# ---------------------------------------------------------------------------
def nova_conexao():
    import pymysql
    config = {
        'user': 'root',
        'password': 'teste',
        'host': '127.0.0.1',
        'database': 'eleicao'
    }

    try:
        conection = pymysql.connect(**config)
        return conection
    except pymysql.err.OperationalError as erro:
        print(f"Erro {erro}")
        return 0
    except:
        print("ERRO DE CONEXÃO DESCONHECIDO.")
        return 0
