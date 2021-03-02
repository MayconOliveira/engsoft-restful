from flask import Flask, g, jsonify, abort, make_response, request
import sqlite3
import src.get
import src.post
import src.put
import src.delete

app = Flask(__name__)

# criando a conexao com a base de dados
def connect_db():
    return sqlite3.connect("db/base_api_cpfweb.db")


# -------------------------
#
# GET
#
# --------------------------

# listando todos os paises
@app.route("/api/paises", methods=["GET"])
def get_paises():
    return src.get.get_paises()


# retorna todos os estados de um país consultando por ID do país
@app.route("/api/paises/<int:pais_id>/estados", methods=["GET"])
def get_estados(pais_id=None):
    return src.get.get_estados(pais_id)


# retorna todas as cidades de um estado consultando por ID do estado
@app.route("/api/estados/<int:estado_id>/cidades", methods=["GET"])
def get_cidades(estado_id=None):
    return src.get.get_cidades(estado_id)


# retorna todos os bairros de uma cidade consultando por ID da cidade
@app.route("/api/cidades/<int:cidade_id>/bairros", methods=["GET"])
def get_bairros(cidade_id=None):
    return src.get.get_bairros(cidade_id)


# retorna todos os endereços
@app.route("/api/enderecos", methods=["GET"])
def get_enderecos():
    return src.get.get_enderecos()


# retorna todos as pessoas
@app.route("/api/pessoas", methods=["GET"])
def get_pessoas():
    return src.get.get_pessoas()


# esse é a rota q o prof pediu no exercício. "dado um CPF, retorne a pessoa e seu endereço completo"
@app.route("/api/pessoas/<string:cpf>", methods=["GET"])
def get_pessoa(cpf=None):
    return src.get.get_pessoa(cpf)


# -------------------------
#
# POST
#
# --------------------------

# criando um país fornecendo um JSON
@app.route("/api/paises", methods=["POST"])
def post_pais():
    return src.post.post_pais()


# criando um estado
@app.route("/api/estados", methods=["POST"])
def post_estado():
    return src.post.post_estado()


# criando um Endereço
@app.route("/api/enderecos", methods=["POST"])
def post_endereco():
    return src.post.post_endereco()


# criando uma pessoa
@app.route("/api/pessoas", methods=["POST"])
def post_pessoa():
    return src.post.post_pessoa()


# -------------------------
#
# PUT
#
# --------------------------

# alterando um país fornecendo um JSON
@app.route("/api/paises/<int:pais_id>", methods=["PUT"])
def put_pais(pais_id=None):
    return src.put.put_pais(pais_id)


# alterando um Endereço fornecendo um JSON
@app.route("/api/enderecos/<int:endereco_id>", methods=["PUT"])
def put_endereco(endereco_id=None):
    return src.put.put_endereco(endereco_id)


# alterando uma Pessoa fornecendo um JSON
@app.route("/api/pessoas/<int:pessoa_id>", methods=["PUT"])
def put_pessoa(pessoa_id=None):
    return src.put.put_pessoa(pessoa_id)


# -------------------------
#
# DELETE
#
# --------------------------


# Removendo um país fornecendo um JSON
@app.route("/api/paises/<int:pais_id>", methods=["DELETE"])
def delete_pais(pais_id=None):
    return src.delete.delete_pais(pais_id)


# Removendo um endereço fornecendo um JSON
@app.route("/api/enderecos/<int:endereco_id>", methods=["DELETE"])
def delete_endereco(endereco_id=None):
    return src.delete.delete_endereco(endereco_id)


# Removendo uma pessoa fornecendo só o ID
@app.route("/api/pessoas/<int:pessoa_id>", methods=["DELETE"])
def delete_pessoa(pessoa_id=None):
    return src.delete.delete_pessoa(pessoa_id)


# adicionando uma rota para dar retorno caso a API seja acessada com um endereço inválido
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Local nao encontrado"}), 404)


if __name__ == "__main__":
    app.run(debug=True)