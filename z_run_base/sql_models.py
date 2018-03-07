# python3 sql_models.py

# # Импортирует классы таблиц
# import sys
# sys.path.append('../butyplastsite')

from run import db, Articles, Products, Maintable
# import sqlalchemy


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
        print(use.maintable.section)
        print("\n-------------------")
        
# print_article()
print("_____________________________")

def print_product():
    """ 
    Печатает данные всей таблицы Articles
    """
    # Запрос к таблице User. Выдаст всех пользователей
    sql_request = Products.query.all()
    # Берет каждого пользователя из запроса
    for use in sql_request :
        print(use.id)
        print(use.slug)
        print(use.created)
        print(use.title)
        print(use.body)
        print(use.specification)
        print(use.image)
        print(use.price)
        print(use.maintable.section)
        print("\n-------------------")
        
# print_product()
print("_____________________________")

def print_maintable():
    """ 
    Печатает данные всей таблицы maintable
    """
    # Запрос к таблице User. Выдаст всех пользователей
    sql_request = Maintable.query.all()
    # Берет каждого пользователя из запроса
    for use in sql_request :
        print(use.id, end=" | ")
        print(use.slug, end=" | ")
        print(use.created, end=" | ")
        print(use.section, end=" | ")
        print(use.link, end=" | ")
        print(use.title_page, end=" | ")
        print(use.data_page)
        for i in use.id_articles:
            print(i.title, end=", ")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        for i in use.id_products:
            print(i.title, end=", ")
        print("\n-------------------------------------------------")
        
# print_maintable()
print("_____________________________")


from math import ceil
class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=3, right_edge=2):
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num
    def list_paginat(self,list_in):
        list_start = self.per_page * (self.page-1) 
        end_list = list_start + self.per_page
        list_out = [i for i in list_in[list_start:end_list]]
        return list_out

                
         




q= 'а'



search_db1 = db.session.query(Products).filter( Products.title.contains(q) |
  Products.body.contains(q) | Products.specification.contains(q)).all()

search_db2 = db.session.query(Articles).filter(Articles.title.contains(q) |
 Articles.body.contains(q) | Articles.specification.contains(q)).all()
 
search_db = search_db1 + search_db2

# print(search_db)
# search_db = ['1','2','3','4','5', '6','7', '8', '9','10','11','12','13','14','15','16','17']

page=3
per_page = 3

total_count = len(search_db)

print(total_count)

pagination = Pagination(page, per_page, total_count)

print(pagination.pages)

print("________________________________")
for i in pagination.iter_pages():
    print(i)
print("________________________________")
list_o = pagination.list_paginat(search_db)
for i in list_o:
    print (i.id, i.title)


# for i in pagination.iter_pages:
#     print(i.id)

# print(pagination.has_prev)

# for row in pages.iter_pages:
#     print(row)

# print(search_db.count())



print("______________________")

# for row in search_db.all():
#     # print(row.id)
#     for i in row:
#         print(i.id)
#     # for i in row.id:
#     #     print(i.price)































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

