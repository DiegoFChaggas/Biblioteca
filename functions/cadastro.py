#Cadastro
import tela_usuario
def cadastrar(conexao,nome,email,senha):
    cursor = conexao.cursor()

    sql = f'INSERT INTO usuarios(usuario_nome,usuario_email, usuario_senha) VALUES (?, ?, ?)' 
    cursor.execute(sql, [nome, email, senha])
    conexao.commit()

    return True
#Login do usuario cadastrado

def login(conexao, email, senha):
    cursor = conexao.cursor()

    sql = f'SELECT * FROM usuarios WHERE usuario_email = ? AND usuario_senha = ?'
    cursor.execute(sql, [email, senha])
    resultado = cursor.fetchone()

    if resultado is None:
        print('Email ou senha incorreto, tente novamente')
        return False
    else: 
        print('Logado com sucesso!')
        tela_usuario.opc_usuario()
        return True