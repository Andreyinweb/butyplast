# python3 run.py

import sys
sys.path.append('../butyplastsite')


from app import app
from models import  db, Articles, Products, Maintable
from generator import Generator
from random import randint, choice
import worddict


def creation_of_database():
    gener = Generator()

    # Удали
    # db.drop_all() # Удали. Это удаляет все таблицы.
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
        new_article = Articles(title= article['title'] , body=article['body'], specification=article['specification'])
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
        new_product = Products(title= product['title'] , body=product['body'], specification=product['specification'], price=randint(10,300))
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

if __name__== '__main__':
    creation_of_database()

















# # Список ролей для таблицы Role
# role_list = ["Admin", "Moderator", "User", "visitor"]

# # Список начальных пользователей
# users_list = ["God", "Son", "Spirit", "Human"]

# # Записывает роли в таблицу Role.(добавляет в сессию базы данных)
# for role in role_list:
#     role_db = Role (name=role) 
#     # Добавляет в сессию базы данных
#     db.session.add(role_db)

# # Записывает пользователей в таблицу User.
# i=1
# for use in users_list:
#     user_db = User (username=use )
#     # Записывает роли связанные по id с таблицей Role. 
#     user_db.role_id =  i
#     # Добавляет в сессию базы данных
#     db.session.add(user_db)    
#     i+=1

# # Записывает случайных пользователей в таблицу User.
# cont = 0
# for i in range(1,randint(3,10)):
#     user_db = User (username=gener.randomnickname())
#     user_db.role_id =  randint(1,4)
#     db.session.add(user_db) 
#     cont = i   


# # Сохраняет  сессию базы данных. 
# # Все ранее добавленное в сесию записывается в таблицы.   
# try:
#     db.session.commit()
#     print("Записаны в базу начальные пользователи.")
#     print(str(cont) + " случайных пользователей записаны в базу.")   
# except :
#     print("Или уже создано или ошибка")


# # Записывает случайные посты в таблицу Post_user.
# cont = 0
# # Берет каждого пользователя из запроса
# for user_db in User.query.all():
#     # Случайное количество постов
#     for i in range(0,randint(1,3)):
#         # Записывает случайные постыю
#         post = gener.randompost()
#         user_post = Post_user(title= post['title'] , body=post['body'])
#         # Записывает пользователей связанные по id с таблицей User.+ str(cont)
#         user_post.user_id=user_db.id
#         # Добавляет в сессию базы данных
#         db.session.add(user_post)
#         cont +=1
# # Сохраняет  сессию базы данных.
# try:
#     db.session.commit()
#     print("Создано " + str(cont) + " ПОСТОВ")   
# except :
#     print("Или уже создано или ошибка")