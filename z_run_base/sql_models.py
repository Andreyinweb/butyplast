# python3 sql_models.py

# Импортирует классы таблиц
import sys
sys.path.append('../butyplastsite')

from models import Articles


def print_article():
    """ 
    Печатает данные всей таблицы Articles
    """
    # Запрос к таблице User. Выдаст всех пользователей
    sql_request = Articles.query.all()
    # Берет каждого пользователя из запроса
    for use in sql_request :
        print(use.id)
        print(use.slug)
        print(use.created)
        print(use.title)
        print(use.body)
        print(use.specification)
        print(use.image)
        print("\n-------------------")
        
print_article()
print("_____________________________")




# def print_user():
#     """ 
#     Печатает данные всей таблицы User(имя 'users')
#     """
#     # Запрос к таблице User. Выдаст всех пользователей
#     sql_request = User.query.all()
#     # Берет каждого пользователя из запроса
#     for use in sql_request :
#         # Печатает строку таблицы User
#         print(use.id, end=". ")
#         print(use.username, end=". ")
#         # Печатает значение из таблицы Role
#         print(use.roles.name, end=". ")
#         print(); print()
#         # Берет каждый пост из запроса к таблице Post_user
#         for post in use.post :
#             # Печатает время создания из таблицы Post_user
#             print(post.created, end="; ")
#         print("\n-------------------")




# def print_role():
#     """
#     Печатает данные всей таблицы Role(имя 'roles')
#     """
#     sql_request = Role.query.all()
#     for roles in sql_request :
#         print(roles.id, end=". ")
#         print(roles.name, end=" : ")
#         for rol in roles.users :
#             print(rol.username, end="; ")
#         print()

# def print_post():
#     """
#     Печатает данные всей таблицы Post_user(имя 'posts')
#     """
#     sql_request = Post_user.query.all()
#     for post in sql_request :
#         print(post.id, end=". ")
#         print(post.title, end=". ")
#         print(post.slug, end=". ")
#         print(post.body, end=". ")
#         print(post.created, end=". ")
#         print(post.user.username, end=". ")
#         print()

# print_user()
# print("_____________________________")
# print_role()
# print("_____________________________")

# print_post()

