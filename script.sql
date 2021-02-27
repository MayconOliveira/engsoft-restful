-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE paises (
id int(11) PRIMARY KEY,
sigla varchar(2),
nome varchar(100)
)

CREATE TABLE enderecos (
id int(11) PRIMARY KEY,
cep varchar(9),
logradouro varchar(100),
numero int(11),
complemento varchar(100),
pais_id int(11),
estado_id int(11),
cidade_id int(11),
bairro_id int(11),
FOREIGN KEY(pais_id) REFERENCES paises (id)
)

CREATE TABLE pessoas (
id int(11) PRIMARY KEY,
cpf varchar(14),
nome varchar(100),
data_nascimento date,
endereco_id int(11),
FOREIGN KEY(endereco_id) REFERENCES enderecos (id)
)

CREATE TABLE estados (
id int(11) PRIMARY KEY,
sigla varchar(2),
nome varchar(100),
pais_id int(11),
FOREIGN KEY(pais_id) REFERENCES paises (id) ON UPDATE CASCADE ON DELETE CASCADE
)

CREATE TABLE cidades (
id int(11) PRIMARY KEY,
sigla varchar(2),
nome varchar(100),
cidade_id int(11),
FOREIGN KEY(cidade_id) REFERENCES estados (id) ON UPDATE CASCADE ON DELETE CASCADE
)

CREATE TABLE bairros (
id int(11) PRIMARY KEY,
sigla varchar(2),
nome varchar(100),
cidade_id int(11),
FOREIGN KEY(cidade_id) REFERENCES cidades (id) ON UPDATE CASCADE ON DELETE CASCADE
)

ALTER TABLE enderecos ADD FOREIGN KEY(estado_id) REFERENCES estados (id)
ALTER TABLE enderecos ADD FOREIGN KEY(cidade_id) REFERENCES cidades (id)
ALTER TABLE enderecos ADD FOREIGN KEY(bairro_id) REFERENCES bairros (id)
