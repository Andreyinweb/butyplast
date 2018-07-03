
# python3 run.py

import sys
sys.path.append('../butyplastsite')
from app import app, db , user_datastore
from models import  Articles, Products, Maintable, Role, User
from generator import Generator
from random import randint, choice
import worddict
import os
import shutil
from PIL import Image

def add_images():
   
    dirname = os.path.abspath(os.path.dirname(__file__))
    # Каталог из которого будем брать файлы 
    directory = dirname + '/images' 
    # Получаем список файлов в переменную 
    images_name = os.listdir(directory)
    # Уменьшение картинки до size
    size = (100, 100)
    for infile in images_name:
        outfile = os.path.splitext(infile)[0] + "_thumb.jpg"
        if infile != outfile:
            try:
                im = Image.open('images/' + infile)
                im.thumbnail(size)
                im.save(os.path.join(app.config['UPLOAD_FOLDER'], outfile), "JPEG")
            except IOError:
                print("cannot create thumbnail for", infile)

    images_name = os.listdir(directory)
    count = 0
    for name in images_name:
        image = directory + '/' + name
        shutil.copy(image, os.path.join(app.config['UPLOAD_FOLDER'], name))
        count += 1
        
    print("Фото скопированы:",count,"шт")

    
def creation_of_database():
    gener = Generator()
    print ("ТУТ создается база?")
    # Удали
    db.drop_all() # Удали. Это удаляет все таблицы.
    # Удали

    # Создает файл базы данных и все таблицы
    db.create_all()
    print("Создана база данных: " + app.config['SQLALCHEMY_DATABASE_URI'] ) 

    # Записывает таблицу Maintable.
    for row in worddict.main_table:
        
        new_row = Maintable(section = row['section'], link = row['link'],
                            title_page = row['title_page'], name_link = row['name_link'], 
                            data_page = row['data_page'])
        # Добавляет в сессию базы данных
        db.session.add(new_row)
    # Записывает случайные статьи в таблицу Articles.
    cont = 0
    # Случайное количество статей
    for i in range(0,randint(2,15)):
        # Записывает случайные статьиS
        article = choice(worddict.articles)
        new_article = Articles(title=article['title'] , body=article['body'], specification=article['specification'],
                               image=article['image'])
        new_article.id_main = 3
        # Добавляет в сессию базы данных
        db.session.add(new_article)
        cont +=1
    # Сохраняет  сессию базы данных.
    try:
        db.session.commit()
        print("Записана база Maintable") 
        print("Создано " + str(cont) + " СТАТЕЙ")   
    except :
        print("Или уже создано или ошибка")

    # Записывает случайные статьи в таблицу Products.
    cont = 0
    # Случайное количество статей
    for i in range(0,randint(10,30)):
        # Записывает случайные статьиS
        product = choice(worddict.products)
        new_product = Products(title= product['title'] , body=product['body'], specification=product['specification'],
                               price=randint(10,300), image=product['image'])
        new_product.id_main = 4
        # Добавляет в сессию базы данных
        db.session.add(new_product)
        cont +=1
    # Сохраняет  сессию базы данных.
    try:
        db.session.commit()
        print("Записано " + str(cont) + " Товаров")   
    except :
        print("Или уже создано или ошибка")
    # Список ролей для таблицы Role
    role_list = {"Admin":"Может все изменять", "Moderator":"Может вносить товары", "User":"Может смотреть корзину", "visitor":"Незнаю зачем"}

    # Список начальных пользователей
    users_list = ["God", "Son", "Spirit", "Human"]

    # Записывает роли в таблицу Role.(добавляет в сессию базы данных)
    for role in role_list:
        role_db = Role (name=role, description = role_list[role]) 
        # Добавляет в сессию базы данных
        db.session.add(role_db)

    # Записывает пользователей в таблицу User.
    i=1
    for use in users_list:
        
        user_db = user_datastore.create_user (username=use, email=use + "@example.lol", password = "admin" , roles=["Admin"])
        # Добавляет в сессию базы данных
        db.session.add(user_db)    
        i+=1

    # Записывает случайных пользователей в таблицу User.
    cont = 0
    for i in range(1,randint(3,10)):
        use = gener.randomnickname()
        user_db = user_datastore.create_user (username=use, email=use + "@example.lol", password = "admin" , roles=["User"])
        db.session.add(user_db) 
        cont = i   

    # Все ранее добавленное в сесию записывается в таблицы.   
    try:
        db.session.commit()
        print("Записаны в базу начальные пользователи.")
        print(str(cont) + " случайных пользователей записаны в базу.")   
    except :
        print("Или уже создано или ошибка")


if __name__== '__main__':
    add_images()
    creation_of_database()
