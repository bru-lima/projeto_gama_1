from flask import Flask, render_template, request, redirect, jsonify
from services.CarregaProduto import CarregaProduto
from services.Carrinho import Carrinho
from services import Produtos
from services import Vendas

carrinho = Carrinho()
app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/management')
def management():
    return render_template('management.html')


@app.route('/management/product')
def product():
    products = CarregaProduto.LoadProduto(app.root_path)
    return render_template('product.html', products=products)


@app.route('/management/product/create', methods=['POST'])
def product_create():
    name = request.form['product-name']
    price = request.form['product-price']
    Produtos.cria(app.root_path, {"nome": name, "preco": price})
    return redirect('/management/product')


@ app.route('/management/product/update', methods=['POST'])
def product_update():
    name = request.form['product-name']
    price = request.form['product-price']
    productId = request.form['product-id']
    # FUNCIONALIDADE DE ATUALIZAR PRODUTO #########################
    return redirect('/management/product')


@ app.route('/management/product/remove', methods=['POST'])
def product_remove():
    productId = request.form['product-id']
    Produtos.deleta(app.root_path, productId)
    return redirect('/management/product')


@ app.route('/management/reports')
def reports():
    vendas = Vendas.get_vendas(app.root_path)
    return render_template('reports.html', vendas=vendas)


@ app.route('/marketplace')
def marketplace():
    carrinho.clear_items()
    products = CarregaProduto.LoadProduto(app.root_path)
    return render_template('marketplace.html', products=products)


@ app.route('/marketplace/add', methods=['POST'])
def marketplace_add():
    product = request.form['product']
    carrinho.adiciona_produto(product)
    return '', 204


@ app.route('/marketplace/remove', methods=['POST'])
def marketplace_remove():
    product = request.form['product']
    carrinho.remove_produto(product)
    return '', 204


@ app.route('/marketplace/submit')
def marketplace_submit():
    items = carrinho.get_items()
    total = carrinho.get_total()
    return render_template('payment.html', items=items, total=total)


@ app.route('/marketplace/submit/success')
def marketplace_success():
    return render_template('payment-conclusion.html')


if (__name__ == '__main__'):
    app.run()
