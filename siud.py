from conecta_banco import nova_conexao as conectar
import pymysql


def inserir_eleitor(nome, cpf, idvoto):
    if conectar() != 0:
        insere_eleitor = f"insert into eleitor (nome, cpf, id_voto) values ('{nome}', '{cpf}', '{idvoto}');"
        insere_voto = f"insert into urna (votos) values ('{idvoto}')"
        with conectar() as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(insere_eleitor)
                cursor.execute(insere_voto)
                conexao.commit()
                return 1
            except pymysql.err.IntegrityError as intg:
                return 2
            except ValueError as e:
                print(e)
                return 0


def buscar_eleitor():
    seleciona = "select eleitor.nome, eleitor.cpf, candidato.nome from eleitor join candidato on id_voto = id_candidato"
    with conectar() as conexao:
        try:
            lista = []
            cursor = conexao.cursor()
            cursor.execute(seleciona)
            for i in cursor.fetchall():
                lista.append(i)
            return lista
        except pymysql.err.IntegrityError as intg:
            print("Erro")
        except:
            print("Erro2")


def resultado_parcial():
    seleciona = """select candidato.nome , urna.votos, count(votos) as total from urna
                    join candidato on urna.votos = candidato.id_candidato
                    group by urna.votos"""
    with conectar() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(seleciona)
            for i in cursor.fetchall():
                print(60 * "-")
                print(f"""Candidato:{i[0]}\n
                      Total de votos: {i[2]} votos.""")
        except pymysql.err.IntegrityError as intg:
            print("Erro")
        except:
            print("Erro2")


def buscar_cpf(cpf):
    seleciona = "select eleitor.cpf from eleitor"
    with conectar() as conexao:
        try:
            lista = []
            cursor = conexao.cursor()
            cursor.execute(seleciona)
            for i in cursor.fetchall():
                if i[0] == cpf:
                    return 0
        except pymysql.err.IntegrityError as intg:
            print("Erro")
        except:
            print("Erro2")


def buscar_idcandidato(candidato):
    seleciona = f"select id_candidato from candidato where nome = '{candidato}'"
    with conectar() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(seleciona)
            for i in cursor.fetchall():
                return i[0]
        except pymysql.err.IntegrityError as intg:
            print("Erro")
        except:
            print("Erro2")
