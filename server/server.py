from flask import Flask, g, jsonify, abort, make_response, request
from flask_cors import CORS
import sqlite3
<<<<<<< HEAD
from flask_cors import CORS
=======
import src.get
import src.post
import src.put
import src.delete
>>>>>>> 57f99af057c0ac63541baaf5e7a2fed9515949ba

app = Flask(__name__)
CORS(app)

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
<<<<<<< HEAD
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
=======
    return src.get.get_pessoas()
>>>>>>> 57f99af057c0ac63541baaf5e7a2fed9515949ba


# esse é a rota q o prof pediu no exercício. "dado um CPF, retorne a pessoa e seu endereço completo"
@app.route("/api/pessoas/<string:cpf>", methods=["GET"])
def get_pessoa(cpf=None):
<<<<<<< HEAD
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
=======
    return src.get.get_pessoa(cpf)
>>>>>>> 57f99af057c0ac63541baaf5e7a2fed9515949ba


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