#Tudo Relacionado aos Livros
import tela_usuario

#Cadastro de livros
def cadastrar_livro(conexao, nome, autor):
    cursor = conexao.cursor()
    sql = f'INSERT INTO livros(livro_nome, livro_autor)VALUES (?, ?)'
    cursor.execute(sql, [nome, autor])    
    conexao.commit()
    return True

#Listar Livros cadastrados
def listar_livros(conexao):
    cursor = conexao.cursor()
    sql = f'SELECT * FROM livros'
    cursor.execute(sql)
    conexao.commit()
    return cursor.fetchall()

#Editar Livro cadastrado
def editar_livro(conexao, nome, nome_novo, autor_novo):
    cursor = conexao.cursor()
    sql = f'UPDATE livros SET livro_nome = ? AND livro_autor = ? WHERE livro_nome = ?'
    cursor.execute(sql, [nome_novo, autor_novo, nome])
    conexao.commit()

    return cursor.fetchall()

#Exluir Livro
def excluir_livro(conexao, id):
    cursor = conexao.cursor()
    sql= f'DELETE FROM livros WHERE id = ?'
    cursor.execute(sql, [id])
    resultado = cursor.fetchone()

    if resultado is None:
        print('Livro não encontrado')
    else: 
        print('Livro excluido com sucesso!')
        tela_usuario.opc_usuario()
        return True

#Alugar Livro
def alugar_livro(conexao, id):
    cursor = conexao.cursor()
    sql = f'SELECT * FROM livros WHERE id = ? AND disponivel = 1'
    cursor.execute(sql, [id])
    resultado = cursor.fetchone()

    if resultado is None:
        print ("O livro não está disponivel para alugar.")
    else:
        sql = f'UPDATE livros SET disponivel = 0 WHERE id = ?'
        cursor.execute(sql, [id])
        conexao.commit()
        print ("Livro alugado com sucesso!")
        tela_usuario.opc_usuario()
        return True

#Devolução de livro alugado
def devolver_livro(conexao, id):
    cursor = conexao.cursor()
    sql = f'SELECT * FROM livros WHERE id = ? AND disponivel = 0'
    cursor.execute(sql, [id])
    resultado = cursor.fetchone()

    if resultado is None:
        print ("O livro não está alugado ou o id foi incorreto.")
    else:
        sql = f'UPDATE livros SET disponivel = 1 WHERE id = ?'
        cursor.execute(sql, [id])
        conexao.commit()
        print ("Livro alugado com sucesso!")
        tela_usuario.opc_usuario()
        return True

#Buscar livros
def buscar_livro(conexao, buscar_nome):
    sql = f'SELECT * FROM livros WHERE livro_nome LIKE ?'
    cursor = conexao.cursor()
    cursor.execute(sql, [f'%{buscar_nome}%'])
    conexao.commit()

    return cursor.fetchall()