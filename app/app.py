from flask import Flask, render_template, request, redirect
from services.CarregaProduto import CarregaProduto

app = Flask(__name__)
carrinho = []


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
    # FUNCIONALIDADE DE CADASTRAR PRODUTO #######################
    print(name, price)
    return redirect('/management/product')


@app.route('/management/product/update', methods=['POST'])
def product_update():
    name = request.form['product-name']
    price = request.form['product-price']
    productId = request.form['product-id']
    # FUNCIONALIDADE DE ATUALIZAR PRODUTO #########################
    print(name, price, productId)
    return redirect('/management/product')


@app.route('/management/product/remove', methods=['POST'])
def product_remove():
    productId = request.form['product-id']
    # FUNCIONALIDADE DE REMOVER ##########################
    print(productId)
    return redirect('/management/product')


@app.route('/marketplace')
def marketplace():
    products = CarregaProduto.LoadProduto(app.root_path)
    return render_template('marketplace.html', products=products)


if (__name__ == '__main__'):
    app.run()
