from flask import Flask, g, jsonify, abort, make_response, request
import sqlite3

app = Flask(__name__)

# ROTAS POST


# criando a conexao com a base de dados
def connect_db():
    return sqlite3.connect("db/base_api_cpfweb.db")


# alterando um país fornecendo um JSON
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
            return jsonify({"success": "Pais atualizado com sucesso!"}), 200
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao atualizar país."}), 400
    finally:
        g.db.close()


# alterando um Endereço fornecendo um JSON
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
            return jsonify({"success": "Endereço atualizado com sucesso!"}), 200
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao atualizar endereço."}), 400
    finally:
        g.db.close()


# alterando uma Pessoa fornecendo um JSON
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
            return jsonify({"success": "Pessoa atualizada com sucesso!"}), 200
    except:
        g.db.rollback()
        return jsonify({"error": "Erro ao atualizar pessoa."}), 400
    finally:
        g.db.close()


if __name__ == "__main__":
    app.run(debug=True)