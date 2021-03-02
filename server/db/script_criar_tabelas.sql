DROP TABLE IF EXISTS paises;
DROP TABLE IF EXISTS enderecos;
DROP TABLE IF EXISTS pessoas;
DROP TABLE IF EXISTS estados;
DROP TABLE IF EXISTS cidades;
DROP TABLE IF EXISTS bairros;
PRAGMA foreign_keys = ON;

CREATE TABLE paises (
id int(11) PRIMARY KEY,
sigla varchar(2),
nome varchar(100)
);

CREATE TABLE estados (
id int(11) PRIMARY KEY,
sigla varchar(2),
nome varchar(100),
pais_id int(11),
FOREIGN KEY(pais_id) REFERENCES paises (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE cidades (
id int(11) PRIMARY KEY,
sigla varchar(2),
nome varchar(100),
estado_id int(11),
FOREIGN KEY(estado_id) REFERENCES estados (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE bairros (
id int(11) PRIMARY KEY,
sigla varchar(2),
nome varchar(100),
cidade_id int(11),
FOREIGN KEY(cidade_id) REFERENCES cidades (id) ON UPDATE CASCADE ON DELETE CASCADE
);

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
FOREIGN KEY(pais_id) REFERENCES paises (id),
FOREIGN KEY(estado_id) REFERENCES estados (id),
FOREIGN KEY(cidade_id) REFERENCES cidades (id),
FOREIGN KEY(bairro_id) REFERENCES bairros (id)
);

CREATE TABLE pessoas (
id int(11) PRIMARY KEY,
cpf varchar(14),
nome varchar(100),
data_nascimento date,
endereco_id int(11),
FOREIGN KEY(endereco_id) REFERENCES enderecos (id)
);

INSERT INTO paises(id,sigla,nome) VALUES (1,'AR','Argentina');
INSERT INTO paises(id,sigla,nome) VALUES (2,'BR','Brasil');
INSERT INTO paises(id,sigla,nome) VALUES (3,'CO','Colômbia');

INSERT INTO estados(id,sigla,nome,pais_id) VALUES (1,'BA','Buenos Aires',1);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (2,'SC','Santa Cruz',1);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (3,'CH','Chubut',1);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (4,'RN','Río Negro',1);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (5,'CO','Córdoba',1);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (6,'AM','Amazonas',2);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (7,'BA','Bahia',2);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (8,'DF','Brasília',2);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (9,'RJ','Rio de Janeiro',2);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (10,'SP','São Paulo',2);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (11,'AQ','Antioquia',3);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (12,'BO','Bolivar',3);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (13,'VC','Valle del Cauca',3);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (14,'SA','Santander',3);
INSERT INTO estados(id,sigla,nome,pais_id) VALUES (15,'TO','Tolima',3);

INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (1,'BA','Buenos Aires',1);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (2,'LP','La Plata',1);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (3,'SI','San Isidro',1);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (4,'BC','Bajo Caracoles',2);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (5,'LG','Laguna Grande',2);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (6,'RG','Río Gallegos',2);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (7,'CR','Comodoro Rivadavia',3);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (8,'PM','Puerto Madrin',3);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (9,'TR','Trelew',3);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (10,'GR','General Roca',4);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (11,'LG','Las Grutas',4);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (12,'MA','Maquinchao',4);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (13,'CO','Ciudad de Córdoba',5);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (14,'RC','Río Cuarto',5);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (15,'VM','Villa María',5);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (16,'MA','Manaus',6);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (17,'TA','Tapauá',6);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (18,'SD','São Domingos',6);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (19,'FS','Feira de Santana',7);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (20,'SA','Salvador',7);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (21,'VC','Vitória da Conquista',7);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (22,'DF','Brasília',8);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (23,'RA','Rajadinha',8);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (24,'SN','Samambaia Norte',8);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (25,'DC','Duque de Caxias',9);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (26,'NI','Niterói',9);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (27,'RJ','Rio de Janeiro',9);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (28,'GU','Guarujá',10);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (29,'SN','Santos',10);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (30,'SA','São Paulo',10);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (31,'ME','Medelín',11);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (32,'SF','Santa Fe de Antioquia',11);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (33,'TU','Turbo',11);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (34,'CI','Cartagena das Índias',12);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (35,'CB','El Carmen de Bolívar',12);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (36,'Ma','Magangué',12);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (37,'BU','Buenaventura',13);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (38,'BG','Buga',13);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (39,'CA','Cali',13);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (40,'BU','Bucaramanga',14);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (41,'BA','Barrancabermeja',14);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (42,'FL','Floridablanca',14);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (43,'CH','Chaparral',15);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (44,'ES','Espinal',15);
INSERT INTO cidades(id,sigla,nome,estado_id) VALUES (45,'IB','Ibagué',15);



INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (1,'BE','Belgrano',1);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (2,'PA','Palermo',1);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (3,'ST','San Telmo',1);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (4,'SL','Altos de San Lorenzo',2);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (5,'ST','Barrio Las Quintas',2);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (6,'TO','Tolosa',2);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (7,'SI','San Isidro',3);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (8,'BC','Bajo Caracoles',4);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (9,'ML','Parque Nacional Monte Leon',5);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (10,'BE','Belgrano',6);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (11,'CC','Caleta Córdova',7);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (12,'PM','Puerto Madrin',8);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (13,'TR','Trelew',9);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (14,'GR','General Roca',10);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (15,'LG','Las Grutas',11);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (16,'MA','Maquinchao',12);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (17,'CO','Ciudad de Córdoba',13);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (18,'RC','Río Cuarto',14);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (19,'VM','Villa María',15);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (20,'AL','Alvorada',16);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (21,'FL','Flores',16);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (22,'NA','Novo Aleixo',16);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (23,'TA','Tapauá',17);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (24,'BB','Bairro Brasil',18);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (25,'CA','Candeias',18);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (26,'IR','Iracema',18);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (27,'CA','Capuchinhos',19);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (28,'JA','Jardim Acácia',19);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (29,'SP','Santo Antônio dos Prazeres',19);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (30,'BR','Brotas',20);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (31,'FE','Federação',20);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (32,'IT','Itaigara',20);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (33,'CE','Centro',21);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (34,'IB','Ibirapuera',21);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (35,'AN','Asa Norte',22);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (36,'AS','Asa Sul',22);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (37,'RA','Rajadinha',23);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (38,'QN','Quadra Norte',24);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (39,'QN','Quadra Sul',24);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (40,'CE','Campos Elíseos',25);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (41,'JP','Jardim Primavera',25);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (42,'SA','Saracuruna',25);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (43,'FO','Fonseca',26);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (44,'IC','Icaraí',26);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (45,'IT','Itaipu',26);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (46,'AB','Alto da Boa Vista',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (47,'BT','Barra da Tijuca',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (48,'BO','Bonsucesso',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (49,'BT','Botafogo',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (50,'CE','Centro',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (51,'CG','Campo Grande',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (52,'CO','Copacabana',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (53,'ES','Estácio',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (54,'FL','Flamengo',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (55,'GL','Glória',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (56,'TI','Tijuca',27);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (57,'BG','Balneário Guarujá',28);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (58,'JP','Jardim dos Pássaros',28);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (59,'CE','Centro',29);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (60,'VB','Vila Belmiro',29);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (61,'VM','Vila Matias',29);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (62,'BR','Brás',30);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (63,'BK','Brooklin',30);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (64,'LI','Liberdade',30);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (65,'MO','Mooca',30);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (66,'MB','Morumbi',30);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (67,'VM','Vila Mariana',30);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (68,'BA','Barcelona',31);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (69,'CA','Calasanz',31);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (70,'LI','Limoncito',31);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (71,'SA','Santa Fe de Antioquia',32);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (72,'TU','Turbo',33);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (73,'BG','Bocagrande',34);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (74,'CB','El Carmen de Bolívar',35);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (75,'MA','Magangué',36);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (76,'BU','Buenaventura',37);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (77,'BG','Buga',38);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (78,'CA','Cali',39);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (79,'BU','Bucaramanga',40);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (80,'BA','Barrancabermeja',41);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (81,'FL','Floridablanca',42);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (82,'CH','Chaparral',43);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (83,'ES','Espinal',44);
INSERT INTO bairros(id,sigla,nome,cidade_id) VALUES (84,'IB','Ibagué',45);



INSERT INTO enderecos(id,cep,logradouro,numero,complemento,pais_id,estado_id,cidade_id,bairro_id) VALUES (1,'B1814XAD','Barrio 1 de Mayo',37,'Casa 3',1,1,1,1);

INSERT INTO pessoas(id,cpf,nome,data_nascimento,endereco_id) VALUES (1,'545.185.360-61','Luiz Gonzaga','1912-12-13',1),(2,'158.286.335-42','Anderson','1912-12-13',1);