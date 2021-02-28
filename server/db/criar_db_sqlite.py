import sqlite3
from sqlite3 import Error

# execute esse arquivo usando python nome_do_arquivo.py pelo Anaconda Prompt. Não esqueça de setar o ambiente antes


def criar_tabelas_popular_db(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cur = conn.cursor()
        sql_file = open("script_criar_tabelas.sql")
        sql_as_string = sql_file.read()
        cur.executescript(sql_as_string)

        print("Tabelas criadas e populadas!")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    criar_tabelas_popular_db(r"base_api_cpfweb.db")
