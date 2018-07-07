# python3 run.py
import sys
sys.path.append('../butyplastsite')
from app import app, db , user_datastore
from models import *
from generator import Generator
from random import randint, choice
import worddict
import os
import shutil
from PIL import Image

def add_images():
   
    dirname = os.path.abspath(os.path.dirname(__file__))
    # The directory from which we will take the files  Каталог из которого будем брать файлы 
    directory = dirname + '/images' 
    # Get the list of files in a variable Получаем список файлов в переменную 
    images_name = os.listdir(directory)
    # Reducing the picture to size Уменьшение картинки до size
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
        
    print("Photo copied:",count)
  
def creation_of_database():
    gener = Generator()
    # Удали
    db.drop_all() # Удали. Это удаляет все таблицы.
    # Удали)

    # Creates all tables. Создает все таблицы
    db.create_all()
    print("Create all tables:  " + app.config['SQLALCHEMY_DATABASE_URI'] ) 

    # Fills the table Maintable. Записывает таблицу Maintable.
    for row in worddict.main_table:
        
        new_row = Maintable(section = row['section'], link = row['link'],
                            title_page = row['title_page'], name_link = row['name_link'], 
                            data_page = row['data_page'])
        # Adds a database session.Добавляет в сессию базы данных
        db.session.add(new_row)

    # Random number of descriptions.Случайное количество описаний
    cont = 0
    for i in range(0,randint(2,15)):
        # Writes random articles. Записывает случайные статьи
        article = choice(worddict.articles)
        new_article = Articles(title=article['title'] , body=article['body'], specification=article['specification'],
                               image=article['image'])
        new_article.id_main = 3
        # Adds a database session. Добавляет в сессию базы данных
        db.session.add(new_article)
        cont +=1
    # Saves the database session. Сохраняет  сессию базы данных.
    try:
        db.session.commit()
        print("Fills the table Maintabl") 
        print("Created: " + str (cont) + " articles")   
    except :
        print("Or already created or an error")

    # Writes random articles to the Products table.
    cont = 0
    # Random number of descriptions. Случайное количество статей
    for i in range(0,randint(10,30)):
        # Writes random product
        product = choice(worddict.products)
        new_product = Products(title= product['title'] , body=product['body'], specification=product['specification'],
                               price=randint(10,300), image=product['image'])
        new_product.id_main = 4
        # Adds a database session. Добавляет в сессию базы данных
        db.session.add(new_product)
        cont +=1
    # Saves the database session. Сохраняет  сессию базы данных.
    try:
        db.session.commit() 
        print("Created: " + str (cont) + " product")   
    except :
        print("Or already created or an error")

    # Role list for the Role table Список ролей для таблицы Role
    role_list = {"Admin":"Может все изменять", "Moderator":"Может вносить товары", "User":"Может смотреть корзину", "visitor":"Незнаю зачем"}

    # List of initial users Список начальных пользователей
    users_list = ["God", "Son", "Spirit", "Human"]

    # Writes roles to the Role table.Записывает роли в таблицу Role.
    for role in role_list:
        role_db = Role (name=role, description = role_list[role]) 
        # Adds a database session. Добавляет в сессию базы данных
        db.session.add(role_db)

    # Writes users to the User table. Записывает пользователей в таблицу User.
    i=1
    for use in users_list:
        email = use.replace(' ', '_') + "@example.lol"
        user_db = user_datastore.create_user (username=use, email=email.lower(), password = "admin" , roles=["Admin"])
        # Adds a database session. Добавляет в сессию базы данных
        db.session.add(user_db)    
        i+=1

    # Writes random users to the User table.Записывает случайных пользователей в таблицу User.
    cont = 0
    for i in range(1,randint(3,10)):
        use = gener.randomnickname()
        email = use.replace(' ', '') + "@example.lol"
        user_db = user_datastore.create_user (username=use, email=email.lower(), password = "admin" , roles=["User"])
        db.session.add(user_db) 
        cont = i   

    # Все ранее добавленное в сесию записывается в таблицы. 
    # All previously added to the session is written to tables  
    try:
        db.session.commit()
        print("The initial users are recorded in the database.")
        print(str(cont) + "  random users are listed in the database.")   
    except :
        print("Or already created or an error")


if __name__== '__main__':
    add_images()
    creation_of_database()
