import json
import pyodbc
 
#print(pyodbc.drivers())
#def conecta_ao_banco(driver,server,database):
#    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database}"
#    return pyodbc.connect(string_conexao)
#
#conexao = conecta_ao_banco('SQL Server','DESKTOP-KK046J1\SQLEXPRESS','eiya_animes')
#print('Conexão bem sucedida')

#comando = conexao.cursor()
#comando.execute('create table teste(id_teste int)')
#comando.commit()
#print('Tabela criada')



from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pagina_inicial.html')

@app.route('/historico')
def historico():
    return render_template('pagina_historico.html')



@app.route('/adm', methods=['GET', 'POST'])
def adm():
    print('Ola')
    if request.method == 'POST':
        print('Entrou')
        req = request.get_json()
        print (req)

        if req['tipoCadastro'] == 'Anime':
            return req['nome_anime']
        

    else:
        print('Fora')
        return render_template('pagina_adm.html')
    

@app.route('/anime')
def pagina_anime():
    return render_template('pagina_anime.html')


#        if tipo == 'novo_anime':
#            nome_anime = request.form['nome_anime']
#            logo_anime = request.form['logo_anime']
#            generos = request.form['generos']
#            descricao = request.form['descricao']
#
#            print(nome_anime)
#
#            novo_anime = {
#                "nome_anime":nome_anime,
#                "logo_anime":logo_anime,
#                "generos":generos,
#                "descricao":descricao
#            }
#            return json.dumps(novo_anime)
#
#        if tipo == 'novo_capitulo':
#            anime_que_capitulo_pertencente = request.form['anime_que_capitulo_pertencente']
#            nome_capitulo = request.form['nome_capitulo']
#            video_capitulo = request.form['video_capitulo']
#            thumbnail = request.form['thumbnail']
#
#            novo_capitulo = {
#                "anime_do_capitulo":anime_que_capitulo_pertencente,
#                "nome_capitulo":nome_capitulo,
#                "video_capitulo":video_capitulo,
#                "thumbnail":thumbnail
#            }
#            return json.dumps(novo_capitulo)        

        
#
#        if nome_anime !='':
#            json.dumps(novo_anime)
#        elif nome_capitulo !='':
#            json.dumps(novo_capitulo)
#        else:
#            return '/erro'
        
#    def verificar(imagem_anime,imagem_fundo_anime,nome_anime,generos,descricao,
#                  anime_do_capitulo,nome_capitulo,video_capitulo,thumbnail):
#        
#        if imagem_anime == '' or nome_anime == '' or generos == '' or descricao =='':
#            if anime_do_capitulo == '' or nome_capitulo == '' or video_capitulo == '' or thumbnail =='':
#                return '/erro'
#            else:
#                if anime_do_capitulo != '' or nome_capitulo != '' or video_capitulo != '' or thumbnail !='':
#                    return json.dumps(novo_capitulo)
#                else: 
#        else:
#            if imagem_anime != '' and nome_anime != '' and generos != '' and descricao !='':
#        
#                return json.dumps(novo_anime)





#@app.route('/cadastro', methods = ['POST', 'GET'])
#def cadastro():
#    if request.method == 'POST':
#        nome = request.form['nome-usuario']
#        email = request.form['email-usuario']
#        senha = request.form['senha-usuario']
#        confirmarSenha = request.form['confirmarSenha-usuario']
#        
#        if senha != confirmarSenha:
#            return redirect(url_for('erro'))
#        else:
#            if os.path.exists(nome + ".txt"):
#                return redirect(url_for('erro'))
#            else: 
#                arquivo_usuario = open(nome + ".txt", "a")
#                arquivo_usuario.write(nome + "\n")
#                arquivo_usuario.write(email + "\n")
#                arquivo_usuario.write(senha + "\n")
#
#            arquivo_usuario = open(nome + ".txt", "r")
#            arquivo_usuario_read = arquivo_usuario.readlines()
#            print(arquivo_usuario_read[0] == nome + "\n")
#            if arquivo_usuario_read[0] == nome + "\n":
#                print('sucesso')
#                return render_template('pagina_login.html')
#    else:
#        return render_template('pagina_cadastro.html')
#            
#        
#
#@app.route('/login', methods = ['POST', 'GET'])
#def login():
#    if request.method == 'POST':
#        nome = request.form['nome-usuario']
#        senha = request.form['senha-usuario']
#
#        arquivo_usuario = open(nome +".txt", "r")
#        arquivo_usuario2 = arquivo_usuario.readlines()
#
#        if nome + "\n" == arquivo_usuario2[0] and senha + "\n" == arquivo_usuario2[2]:
#            return  redirect(url_for('historico'))
#        else:
#            return "Usuário ou senha incorretos, tente novamente"
#    else:
#        return render_template('pagina_login.html')

app.run(debug=True)