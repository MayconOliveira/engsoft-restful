from flask import Flask, g, jsonify, abort, make_response, request
import sqlite3

app = Flask(__name__)

# ROTAS POST


# criando a conexao com a base de dados
def connect_db():
    return sqlite3.connect("db/base_api_cpfweb.db")


# criando um país fornecendo um JSON
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


# criando um estado
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




if __name__ == "__main__":
    app.run(debug=True)