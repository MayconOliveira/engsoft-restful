from flask import Flask, g, jsonify, abort, make_response, request
import sqlite3

app = Flask(__name__)

# ROTAS GET


# criando a conexao com a base de dados
def connect_db():
    return sqlite3.connect("db/base_api_cpfweb.db")


# listando todos os paises
def get_paises():
    g.db = connect_db()
    cur = g.db.execute("select id,sigla,nome from paises")
    paises = [
        dict(
            id=row[0],
            sigla=row[1],
            nome=row[2],
        )
        for row in cur.fetchall()
    ]
    g.db.close()
    return jsonify({"paises": paises})


# retorna todos os estados de um país consultando por ID do país
def get_estados(pais_id=None):
    g.db = connect_db()
    cur = g.db.execute(
        "select e.id,e.sigla,e.nome,e.pais_id from estados e inner join paises p on e.pais_id=p.id where p.id = ?",
        [pais_id],
    )
    estados = [
        dict(
            id=row[0],
            sigla=row[1],
            nome=row[2],
            pais_id=row[3],
        )
        for row in cur.fetchall()
    ]
    g.db.close()
    return jsonify({"estados": estados})


# retorna todas as cidades de um estado consultando por ID do estado
def get_cidades(estado_id=None):
    g.db = connect_db()
    cur = g.db.execute(
        "select c.id,c.sigla,c.nome,c.estado_id from cidades c inner join estados e on c.estado_id=e.id where e.id = ?",
        [estado_id],
    )
    cidades = [
        dict(
            id=row[0],
            sigla=row[1],
            nome=row[2],
            estado_id=row[3],
        )
        for row in cur.fetchall()
    ]
    g.db.close()
    return jsonify({"cidades": cidades})


# retorna todos os bairros de uma cidade consultando por ID da cidade
def get_bairros(cidade_id=None):
    g.db = connect_db()
    cur = g.db.execute(
        "select b.id,b.sigla,b.nome,b.cidade_id from bairros b inner join cidades c on b.cidade_id=c.id where c.id = ?",
        [cidade_id],
    )
    bairros = [
        dict(
            id=row[0],
            sigla=row[1],
            nome=row[2],
            cidade_id=row[3],
        )
        for row in cur.fetchall()
    ]
    g.db.close()
    return jsonify({"bairros": bairros})


# retorna todos os endereços
def get_enderecos():
    g.db = connect_db()
    cur = g.db.execute(
        "SELECT id, cep, logradouro, numero, complemento, pais_id, estado_id, cidade_id, bairro_id FROM enderecos"
    )
    enderecos = [
        dict(
            id=row[0],
            cep=row[1],
            logradouro=row[2],
            numero=row[3],
            complemento=row[4],
            pais_id=row[5],
            estado_id=row[6],
            cidade_id=row[7],
            bairro_id=row[8],
        )
        for row in cur.fetchall()
    ]
    g.db.close()
    return jsonify({"enderecos": enderecos})


# retorna todos as pessoas
def get_pessoas():
    g.db = connect_db()
    cur = g.db.execute(
        "SELECT id, cpf, nome, data_nascimento, endereco_id FROM pessoas"
    )
    pessoas = [
        dict(
            id=row[0],
            cpf=row[1],
            nome=row[2],
            data_nascimento=row[3],
            endereco_id=row[4],
        )
        for row in cur.fetchall()
    ]
    g.db.close()
    return jsonify({"pessoas": pessoas})


# esse é a rota q o prof pediu no exercício. "dado um CPF, retorne a pessoa e seu endereço completo"
def get_pessoa(cpf=None):
    g.db = connect_db()
    # precisamos definir esse último separador como traço. Pq já vi gente usando barra tb. De repente o cliente tratava isso e enviava a string com pontos e traços?
    cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]
    campos = "pe.id,cpf,pe.nome as nome_pessoa,strftime('%d/%m/%Y',data_nascimento) as data_nascimento,cep,logradouro,numero,complemento,pa.sigla as pais_sigla,pa.nome as pais_nome,es.sigla as estado_sigla,es.nome as estado_nome,c.sigla as cidade_sigla,c.nome as cidade_nome,b.sigla as bairro_sigla,b.nome as bairro_nome"
    joins = "inner join enderecos en on pe.endereco_id=en.id inner join paises pa on en.pais_id=pa.id inner join estados es on en.estado_id=es.id inner join cidades c on en.cidade_id=c.id inner join bairros b on en.bairro_id=b.id"
    cur = g.db.execute(
        f" SELECT {campos} FROM pessoas pe {joins} where pe.cpf = ?", [cpf]
    )
    pessoa = [
        dict(
            id=row[0],
            cpf=row[1],
            nome_pessoa=row[2],
            data_nascimento=row[3],
            cep=row[4],
            logradouro=row[5],
            numero=row[6],
            complemento=row[7],
            pais_sigla=row[8],
            pais_nome=row[9],
            estado_sigla=row[10],
            estado_nome=row[11],
            cidade_sigla=row[12],
            cidade_nome=row[13],
            bairro_sigla=row[14],
            bairro_nome=row[15],
        )
        for row in cur.fetchall()
    ]
    g.db.close()
    return jsonify({"pessoa": pessoa})
    return jsonify(
        {"pessoa": cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]}
    )


if __name__ == "__main__":
    app.run(debug=True)