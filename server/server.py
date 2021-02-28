from flask import Flask, g, jsonify, abort, make_response
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
    # como o campo CPF tem 14 caracteres, é pra ser gravado com pontos e traços. Não é uma boa prática, mas dps a gente ajusta melhor.
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


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/todo/api/tasks", methods=["POST"])
def get_tasks():
    return jsonify({"tasks": tasks})


"""
@app.route("/todo/api/tasks", methods=["POST"])
def create_task():
    if not request.json or not "title" in request.json:
        abort(400)
    task = {
        "id": tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False,
    }
    tasks.append(task)
    return jsonify({"task": task}), 201"""
