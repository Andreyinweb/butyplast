# -*- coding: utf-8 -*-
from random import randint, sample, choice
from worddict import nickname, posts

class Generator():
    """Generator of random users
    Генератор случайных пользователей"""

    def __init__(self, login_length=5, password_length=12, dict_user={}):
        self.dict_user = dict_user
        self.login_length = login_length
        self.password_length = password_length
        self.leter_number = [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]+\
                [str(x) for x in range(0,10)]


    def randomword(self,length = 0):
        """Generates a random sequence
        given length
        Генерирует случайную последовательность символов
        заданной длины"""
        if length == 0: lengt = self.password_length
        gen = sample( self.leter_number, length)
        word = ''
        for i in gen:
            word += i
        return word

    def randomlogin(self,length = 0):
        """Generates a random sequence of characters
        specified length
        Генерирует случайную последовательность символов
        заданной длины"""
        if length == 0:
             length = self.login_length
        login = self.randomword(length) 
        return login

    def newuser(self, login_length=0, password_length = 0):
        """Generates login, password
        Генерирует login, password"""
        if login_length == 0:login_length = self.login_length
        login = self.randomlogin(login_length)
        if password_length == 0: password_length = self.password_length
        password = self.randomword(password_length)
        return login, password

    def list_user (self, length=1):
        """Generates a user dictionary of length (length) {login: password}
        Генерирует словарь пользователей длины length {login: password}"""
        for i in range(0,length):
            key, value = self.newuser()
            self.dict_user.update({key: value})
        return self.dict_user

    def randomtext(self,length_text=10, length = 0):
        """
        Генерирует случайнный текст
        заданной длины"""
        if length == 0: 
            length = self.login_length
        text = ""
        for i in range(0, length_text):
            text += self.randomword(length) + ' '
        return text

    def randomnickname(self):
        """Generates a random nickname
        Генерирует случайноу имя"""
        login = choice( nickname)
        return login

    def randompost(self):
        """Generates a random post
        Генерирует случайноу post"""
        post = choice( posts)
        return post




