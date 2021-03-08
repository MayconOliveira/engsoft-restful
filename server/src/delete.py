from flask import Flask, g, jsonify, abort, make_response, request
import sqlite3

app = Flask(__name__)

# ROTAS POST


# criando a conexao com a base de dados
def connect_db():
    return sqlite3.connect("db/base_api_cpfweb.db")


# Removendo um país fornecendo um JSON
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


# Removendo uma pessoa fornecendo só o ID
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