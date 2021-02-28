from flask import Flask, g, jsonify, abort, make_response, request
import sqlite3

app = Flask(__name__)

# criando a conexao com a base de dados
def connect_db():
    return sqlite3.connect("db/base_api_cpfweb.db")


# GET

# listando todos os paises
@app.route("/paises", methods=["GET"])
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
@app.route("/paises/<int:pais_id>/estados", methods=["GET"])
def get_estado(pais_id=None):
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
    return jsonify({"estado": estados})


# esse é a rota q o prof pediu no exercício. "dado um CPF, retorne a pessoa e seu endereço completo"
@app.route("/pessoas/<string:cpf>", methods=["GET"])
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


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Local nao encontrado"}), 404)


# POST

# criando um país fornecendo um JSON
@app.route("/paises", methods=["POST"])
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
"""@app.route("/paises", methods=["POST"])
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
@app.route("/estados", methods=["POST"])
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


# PUT

# alterando um país fornecendo um JSON
@app.route("/paises/<int:pais_id>", methods=["PUT"])
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
        g.db.execute(
            "UPDATE paises SET sigla = ?, nome = ? where id = ?",
            (pais_sigla, pais_nome, pais_id_uri),
        )

        g.db.commit()
        return jsonify({"success": "Pais atualizado com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao atualizar país."}), 400
    finally:
        g.db.close()


# DELETE


# alterando um país fornecendo um JSON
@app.route("/paises/<int:pais_id>", methods=["DELETE"])
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
        g.db.execute(
            "DELETE FROM paises where id = ?",
            [pais_id_uri],
        )

        g.db.commit()
        return jsonify({"success": "Pais removido com sucesso!"}), 201
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao remover país."}), 400
    finally:
        g.db.close()


if __name__ == "__main__":
    app.run(debug=True)