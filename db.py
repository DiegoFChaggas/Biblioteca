#Criação das Tabelas
import sqlite3

conn = sqlite3.connect('biblioteca_db') 
cursor = conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_nome VARCHAR(25),
            usuario_email VARCHAR(50),
            usuario_senha VARCHAR(25)
            )
            ''')
cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY,
            livro_nome VARCHAR(50),
            livro_autor VARCHAR(50),
            disponivel INTEGER DEFAULT 1,
            usuario_id INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
            ''')
conn.commit()