from app import app 
import view
from goods.blueprint import goods
from articles.blueprint import articles
from services.blueprint import services


app.register_blueprint(goods, url_prefix='/goods')
app.register_blueprint(articles, url_prefix='/articles')
app.register_blueprint(services, url_prefix='/services')


if __name__ == '__main__':
    app.run()