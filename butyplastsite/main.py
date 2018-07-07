from app import app
import view
from products.blueprint import products
from articles.blueprint import articles

app.register_blueprint(products, url_prefix='/products')
app.register_blueprint(articles, url_prefix='/articles')

if __name__ == '__main__':
    app.run()