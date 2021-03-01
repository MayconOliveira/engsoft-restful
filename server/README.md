# Web service da API CPF Web

Este web service, escrito em Python, permite obter dados sobre uma pessoa buscando pelo seu CPF.

## Instalação

Antes de começar, você precisa de um gerenciador de ambientes como o [Anaconda](https://www.anaconda.com/products/individual#windows) para através dele instalar o Python e todas as outras dependências do seu projeto.
Para propósitos acadêmicos só iremos mostrar o processo de instalação no Windows, mas outras plataformas também são suportadas. Veja [aqui](https://docs.anaconda.com/anaconda/install/).

Com o Anaconda instalado, você precisa criar um ambiente. É nele que todos os pacotes ficarão. Abra o Anaconda Prompt e digite:
```
$ conda create --name nome_do_seu_ambiente python=3.7
```
Caso o nosso nome de ambiente seja "cpfweb", o código acima ficaria:
```
$ conda create --name cpfweb python=3.7
```

Com o ambiente criado, vamos ativá-lo e instalar o pacote [Flask](https://flask.palletsprojects.com/en/1.1.x/), [sqlite3](https://anaconda.org/blaze/sqlite3)

```
$ conda activate cpfweb
(cpfweb) $ conda install flask
(cpfweb) $ conda install -c blaze sqlite3
```


## Uso
Abra o Anaconda Prompt, navegue até a pasta ``server\db`` e execute:
```
(cpfweb) $ python criar_db_sqlite.py 
```
Após isso surgirá o arquivo ``base_api_cpfweb.db`` contendo todas as tabelas necessárias, bem como uma carga inicial de dados, para que o web service seja consumido.

Após isso, ainda pelo Anaconda Prompt, volte à pasta ``server`` e execute:

```python
(cpfweb) $ python server.py
```
A partir de então, o servidor está rodando e a API, pronta para ser consumida.

Iremos dar instruções para os testes via [Postman](https://go.postman.co/)


## Contribuições
Pull requests são bem vindos. Para mudanças maiores, por favor crie um novo issue antes para que possamos discutir o que você pretende mudar. 


## Licença
[MIT](https://choosealicense.com/licenses/mit/)