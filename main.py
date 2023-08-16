from flask import Flask, render_template, redirect, request, Response, jsonify, url_for
import database as dbase
from produto import Produto

db = dbase.dbConnect()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AGATHAAPP'

#HOME
@app.route("/")
def home():
    produtos = db['produtos']
    produtosRecebidos = produtos.find()

    return render_template("home.html", products=produtosRecebidos)


#Method POST
@app.route("/produtos", methods=['POST'])
def addProduto():
    produtos = db['produtos']
    nome = request.form['nome']
    preco = request.form['preco']
    quantidade = request.form['quantidade']

    if nome and preco and quantidade:
        produto = Produto(nome, preco, quantidade)
        produtos.insert_one(produto.toBDColletion())
        response = jsonify({
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        })
        return redirect(url_for('home'))
    else:
        return not_Found()


#Method Delete
@app.route("/delete/<string:produto_nome>")
def delete(produto_nome):
    produtos = db['produtos']
    produtos.delete_one({'nome': produto_nome})
    return redirect(url_for('home'))


#Method PUT
@app.route("/edit/<string:produto_nome>", methods=['POST'])
def edit(produto_nome):
    produtos = db['produtos']
    nome = request.form['nome']
    preco = request.form['preco']
    quantidade = request.form['quantidade']

    if nome and preco and quantidade:
        produtos.update_one({'nome': produto_nome}, {'$set': {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }})
        response = jsonify({'mensagem': 'Produto ' + produto_nome + ' atualizado corretamente!'})
        return redirect(url_for('home'))
    else:
        return not_Found()
    

#ERROR
@app.errorhandler(404)
def not_Found(error=None):
    mensagem = {
        'mensagem': 'Não encontardo ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(mensagem)
    response.status_code = 404
    return response


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


