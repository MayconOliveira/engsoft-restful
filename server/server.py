from flask import Flask, g, jsonify, abort, make_response, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# criando a conexao com a base de dados
def connect_db():
    return sqlite3.connect("db/base_api_cpfweb.db")


# GET

# listando todos os paises
@app.route("/api/paises", methods=["GET"])
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
@app.route("/api/paises/<int:pais_id>/estados", methods=["GET"])
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
@app.route("/api/estados/<int:estado_id>/cidades", methods=["GET"])
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
@app.route("/api/cidades/<int:cidade_id>/bairros", methods=["GET"])
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
@app.route("/api/enderecos", methods=["GET"])
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
@app.route("/api/pessoas", methods=["GET"])
def get_pessoas():
    g.db = connect_db()
    campos = "pe.id,cpf,pe.nome as nome_pessoa,strftime('%d/%m/%Y',data_nascimento) as data_nascimento,cep,logradouro,numero,complemento,pa.sigla as pais_sigla,pa.nome as pais_nome,es.sigla as estado_sigla,es.nome as estado_nome,c.sigla as cidade_sigla,c.nome as cidade_nome,b.sigla as bairro_sigla,b.nome as bairro_nome"
    joins = "inner join enderecos en on pe.endereco_id=en.id inner join paises pa on en.pais_id=pa.id inner join estados es on en.estado_id=es.id inner join cidades c on en.cidade_id=c.id inner join bairros b on en.bairro_id=b.id"
    cur = g.db.execute(
        f" SELECT {campos} FROM pessoas pe {joins}"
    )
    pessoas = [
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
    return jsonify({"pessoas": pessoas})


# esse é a rota q o prof pediu no exercício. "dado um CPF, retorne a pessoa e seu endereço completo"
@app.route("/api/pessoas/<string:cpf>", methods=["GET"])
def get_pessoa(cpf=None):
    g.db = connect_db()
    # precisamos definir esse último separador como traço. Pq já vi gente usando barra tb. De repente o cliente tratava isso e enviava a string com pontos e traços?
   
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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Local nao encontrado"}), 404)


# POST

# criando um país fornecendo um JSON
@app.route("/api/paises", methods=["POST"])
def post_pais():
    if not request.json or not "pais" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)
    try:
        pais_id = request.json["pais"]["id"]
        pais_sigla = request.json["pais"]["sigla"]
        pais_nome = request.json["pais"]["nome"]

        g.db = connect_db()
        g.db.execute(
            "INSERT INTO paises (id,sigla,nome) VALUES (?,?,?)",
            (pais_id, pais_sigla, pais_nome),
        )

        g.db.commit()
        return jsonify({"success": "Pais cadastrado com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao cadastrar país."}), 400
    finally:
        g.db.close()


# criando um país com dados vindos de um formdata
"""@app.route("/api/paises", methods=["POST"])
def post_pais():
    try:
        pais_id = request.form["id"]
        pais_sigla = request.form["sigla"]
        pais_nome = request.form["nome"]

        g.db = connect_db()
        g.db.execute(
            "INSERT INTO paises (id,sigla,nome) VALUES (?,?,?)",
            (pais_id, pais_sigla, pais_nome),
        )

        g.db.commit()

        return jsonify({"success": "Pais cadastrado com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao cadastrar país."}), 400

    finally:
        g.db.close()"""


# criando um estado
@app.route("/api/estados", methods=["POST"])
def post_estado():
    if not request.json or not "estado" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)
    try:
        estado_id = request.json["estado"]["id"]
        estado_sigla = request.json["estado"]["sigla"]
        estado_nome = request.json["estado"]["nome"]
        estado_pais_id = request.json["estado"]["pais_id"]

        g.db = connect_db()
        g.db.execute(
            "INSERT INTO estados (id,sigla,nome,pais_id) VALUES (?,?,?,?)",
            (estado_id, estado_sigla, estado_nome, estado_pais_id),
        )

        g.db.commit()
        return jsonify({"success": "Estado cadastrado com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao cadastrar estado."}), 400

    finally:
        g.db.close()


# criando um Endereço
@app.route("/api/enderecos", methods=["POST"])
def post_endereco():
    if not request.json or not "endereco" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)
    try:
        endereco_id = request.json["endereco"]["id"]
        endereco_cep = request.json["endereco"]["cep"]
        endereco_logradouro = request.json["endereco"]["logradouro"]
        endereco_numero = request.json["endereco"]["numero"]
        endereco_complemento = request.json["endereco"]["complemento"]
        endereco_pais_id = request.json["endereco"]["pais_id"]
        endereco_estado_id = request.json["endereco"]["estado_id"]
        endereco_cidade_id = request.json["endereco"]["cidade_id"]
        endereco_bairro_id = request.json["endereco"]["bairro_id"]

        g.db = connect_db()
        g.db.execute(
            "INSERT INTO enderecos (id, cep, logradouro, numero, complemento, pais_id, estado_id, cidade_id, bairro_id) VALUES (?,?,?,?,?,?,?,?,?)",
            (
                endereco_id,
                endereco_cep,
                endereco_logradouro,
                endereco_numero,
                endereco_complemento,
                endereco_pais_id,
                endereco_estado_id,
                endereco_cidade_id,
                endereco_bairro_id,
            ),
        )

        g.db.commit()
        return jsonify({"success": "Endereço cadastrado com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao cadastrar endereço."}), 400

    finally:
        g.db.close()


# criando uma pessoa
@app.route("/api/pessoas", methods=["POST"])
def post_pessoa():
    if not request.json or not "pessoa" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)
    try:
        pessoa_id = request.json["pessoa"]["id"]
        pessoa_cpf = request.json["pessoa"]["cpf"]
        pessoa_nome = request.json["pessoa"]["nome"]
        data_nascimento_id = request.json["pessoa"]["data_nascimento"]
        pessoa_pais_id = request.json["pessoa"]["endereco_id"]

        g.db = connect_db()
        g.db.execute(
            "INSERT INTO pessoas (id,cpf,nome,data_nascimento,endereco_id) VALUES (?,?,?,?,?)",
            (pessoa_id, pessoa_cpf, pessoa_nome, data_nascimento_id, pessoa_pais_id),
        )

        g.db.commit()
        return jsonify({"success": "Pessoa cadastrado com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao cadastrar pessoa."}), 400

    finally:
        g.db.close()


# PUT

# alterando um país fornecendo um JSON
@app.route("/api/paises/<int:pais_id>", methods=["PUT"])
def put_pais(pais_id=None):
    # aqui eu verifico se o payload é JSON e se é referente a País
    if not request.json or not "pais" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)

    # aqui eu verifico se a Id enviada pelo payload confere com a id fornecida na URI
    # segundo o padrão RFC 7231 da IETF https://tools.ietf.org/html/rfc7231#section-4.3.4
    pais_id_uri = request.json["pais"]["id"]
    if pais_id != pais_id_uri:
        return make_response(
            jsonify({"error": "Id da payload não confere com a Id da URI."}), 404
        )

    try:
        pais_sigla = request.json["pais"]["sigla"]
        pais_nome = request.json["pais"]["nome"]

        g.db = connect_db()
        # criando um cursor para depois podermos averiguar se a query abaixo realmente aconteceu
        cur = g.db.cursor()
        cur.execute(
            "UPDATE paises SET sigla = ?, nome = ? where id = ?",
            (pais_sigla, pais_nome, pais_id_uri),
        )

        g.db.commit()

        if cur.rowcount == 0:
            return (
                jsonify(
                    {
                        "error": "Erro ao atualizar país. O país informado talvez não exista."
                    }
                ),
                400,
            )
        elif cur.rowcount == 1:
            return jsonify({"success": "Pais atualizado com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao atualizar país."}), 400
    finally:
        g.db.close()


# alterando um Endereço fornecendo um JSON
@app.route("/api/enderecos/<int:endereco_id>", methods=["PUT"])
def put_endereco(endereco_id=None):
    # aqui eu verifico se o payload é JSON e se é referente a País
    if not request.json or not "endereco" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)

    # aqui eu verifico se a Id enviada pelo payload confere com a id fornecida na URI
    # segundo o padrão RFC 7231 da IETF https://tools.ietf.org/html/rfc7231#section-4.3.4
    endereco_id_uri = request.json["endereco"]["id"]
    if endereco_id != endereco_id_uri:
        return make_response(
            jsonify({"error": "Id da payload não confere com a Id da URI."}), 404
        )

    try:
        endereco_cep = request.json["endereco"]["cep"]
        endereco_logradouro = request.json["endereco"]["logradouro"]
        endereco_numero = request.json["endereco"]["numero"]
        endereco_complemento = request.json["endereco"]["complemento"]
        endereco_pais_id = request.json["endereco"]["pais_id"]
        endereco_estado_id = request.json["endereco"]["estado_id"]
        endereco_cidade_id = request.json["endereco"]["cidade_id"]
        endereco_bairro_id = request.json["endereco"]["bairro_id"]

        g.db = connect_db()
        # criando um cursor para depois podermos averiguar se a query abaixo realmente aconteceu
        cur = g.db.cursor()
        cur.execute(
            "UPDATE enderecos SET cep = ?,logradouro = ?,numero = ?,complemento = ?,pais_id = ?,estado_id = ?,cidade_id = ?,bairro_id = ? where id = ?",
            (
                endereco_cep,
                endereco_logradouro,
                endereco_numero,
                endereco_complemento,
                endereco_pais_id,
                endereco_estado_id,
                endereco_cidade_id,
                endereco_bairro_id,
                endereco_id_uri,
            ),
        )

        g.db.commit()

        if cur.rowcount == 0:
            return (
                jsonify(
                    {
                        "error": "Erro ao atualizar endereço. O endereço informado talvez não exista."
                    }
                ),
                400,
            )
        elif cur.rowcount == 1:
            return jsonify({"success": "Endereço atualizado com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao atualizar endereço."}), 400
    finally:
        g.db.close()


# alterando uma Pessoa fornecendo um JSON
@app.route("/api/pessoas/<int:pessoa_id>", methods=["PUT"])
def put_pessoa(pessoa_id=None):
    # aqui eu verifico se o payload é JSON e se é referente a País
    if not request.json or not "pessoa" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)

    # aqui eu verifico se a Id enviada pelo payload confere com a id fornecida na URI
    # segundo o padrão RFC 7231 da IETF https://tools.ietf.org/html/rfc7231#section-4.3.4
    pessoa_id_uri = request.json["pessoa"]["id"]
    if pessoa_id != pessoa_id_uri:
        return make_response(
            jsonify({"error": "Id da payload não confere com a Id da URI."}), 404
        )

    try:
        pessoa_cpf = request.json["pessoa"]["cpf"]
        pais_nome = request.json["pessoa"]["nome"]
        pessoa_data_nascimento = request.json["pessoa"]["data_nascimento"]
        pessoa_endereco_id = request.json["pessoa"]["endereco_id"]

        g.db = connect_db()
        # criando um cursor para depois podermos averiguar se a query abaixo realmente aconteceu
        cur = g.db.cursor()
        cur.execute(
            "UPDATE pessoas SET cpf = ?, nome = ?, data_nascimento = ?, endereco_id = ?  where id = ?",
            (
                pessoa_cpf,
                pais_nome,
                pessoa_data_nascimento,
                pessoa_endereco_id,
                pessoa_id_uri,
            ),
        )

        g.db.commit()

        if cur.rowcount == 0:
            return (
                jsonify(
                    {
                        "error": "Erro ao atualizar pessoa. A pessoa informada talvez não exista."
                    }
                ),
                400,
            )
        elif cur.rowcount == 1:
            return jsonify({"success": "Pessoa atualizada com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao atualizar pessoa."}), 400
    finally:
        g.db.close()


# DELETE


# Removendo um país fornecendo um JSON
@app.route("/api/paises/<int:pais_id>", methods=["DELETE"])
def delete_pais(pais_id=None):
    # aqui eu verifico se o payload é JSON e se é referente a País
    if not request.json or not "pais" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)

    # aqui eu verifico se a Id enviada pelo payload confere com a id fornecida na URI
    # segundo o padrão RFC 7231 da IETF https://tools.ietf.org/html/rfc7231#section-4.3.4
    pais_id_uri = request.json["pais"]["id"]
    if pais_id != pais_id_uri:
        return make_response(
            jsonify({"error": "Id da payload não confere com a Id da URI."}), 404
        )

    try:
        g.db = connect_db()
        cur = g.db.cursor()
        cur.execute(
            "DELETE FROM paises where id = ?",
            [pais_id_uri],
        )

        g.db.commit()
        if cur.rowcount == 0:
            return (
                jsonify(
                    {
                        "error": "Erro ao remover país. O país informado talvez não exista."
                    }
                ),
                400,
            )
        elif cur.rowcount == 1:
            return jsonify({"success": "Pais removido com sucesso!"}), 201

    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao remover país."}), 400
    finally:
        g.db.close()


# Removendo um endereço fornecendo um JSON
@app.route("/api/enderecos/<int:endereco_id>", methods=["DELETE"])
def delete_endereco(endereco_id=None):
    # aqui eu verifico se o payload é JSON e se é referente a País
    if not request.json or not "endereco" in request.json:
        return make_response(jsonify({"error": "JSON não fornecido"}), 404)

    # aqui eu verifico se a Id enviada pelo payload confere com a id fornecida na URI
    # segundo o padrão RFC 7231 da IETF https://tools.ietf.org/html/rfc7231#section-4.3.4
    endereco_id_uri = request.json["endereco"]["id"]
    if endereco_id != endereco_id_uri:
        return make_response(
            jsonify({"error": "Id da payload não confere com a Id da URI."}), 404
        )

    try:
        g.db = connect_db()
        cur = g.db.cursor()
        cur.execute(
            "DELETE FROM enderecos where id = ?",
            [endereco_id_uri],
        )

        g.db.commit()
        if cur.rowcount == 0:
            return (
                jsonify(
                    {
                        "error": "Erro ao remover endereco. O endereco informado talvez não exista."
                    }
                ),
                400,
            )
        elif cur.rowcount == 1:
            return jsonify({"success": "Endereço removido com sucesso!"}), 201

    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao remover endereço."}), 400
    finally:
        g.db.close()


# Removendo uma pessoa fornecendo um JSON
@app.route("/api/pessoas/<int:pessoa_id>", methods=["DELETE"])
def delete_pessoa(pessoa_id=None):
   
    try:
        g.db = connect_db()
        cur = g.db.cursor()
        cur.execute(
            "DELETE FROM pessoas where id = ?",
            [pessoa_id],
        )

        g.db.commit()
        if cur.rowcount == 0:
            return (
                jsonify(
                    {
                        "error": "Erro ao remover pessoa. A pessoa informada talvez não exista."
                    }
                ),
                400,
            )
        elif cur.rowcount == 1:
            return jsonify({"success": "Pessoa removida com sucesso!"}), 201

    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao remover pessoa."}), 400
    finally:
        g.db.close()


if __name__ == "__main__":
    app.run(debug=True)