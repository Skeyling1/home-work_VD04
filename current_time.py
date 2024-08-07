#Задание 1
#Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной странице.

from flask import Flask
from datetime import datetime


app = Flask(__name__) #сохраняем в неё объект класса Flask

@app.route("/") #декоратор для ссылки и URL-адреса.
def cur_time():
    cur_data_time = datetime.now()
    frmtd_data_time = cur_data_time.strftime("%Y-%m-%d %H:%M:%S")
    return (f"Сейчас {frmtd_data_time}")


if __name__ == "__main__":
    app.run() #Делаем запуск. Прописываем условие проверки. Если данный скрипт выполнен напрямую (из файла), то запускается локальный сервер (на нашем компьютере).