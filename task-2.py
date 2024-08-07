#Задание 2
#Создайте новое приложение Flask, создайте структуру проекта с папками static и templates,
# в папке templates должны быть 3 html файла: index, blog, contacts (главная страница, страница блога и контакты).
# Заполните их информацией и выведите силами flask сервера, используя функцию render_template()
#Обязательно на всех страницах сделайте меню, которое будет работать именно при запуске проекта через flask
import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return flask.render_template("index.html")

@app.route("/blog/")
def blog():
    return flask.render_template("blog.html")

@app.route("/contacts/")
def contact():
    return flask.render_template("contacts.html")

if __name__ == "__main__":
    app.run()