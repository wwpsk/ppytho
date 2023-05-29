from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import datetime

# Получаем HTML-код страницы с погодой в Мариуполе
url = "https://sinoptik.ua/погода-мариуполь"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Находим информацию о температуре
    temperature_element = soup.find(class_="today-temp")
    if temperature_element is not None:
        temperature = temperature_element.text
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Соединяемся с базой данных или создаем ее, если она не существует
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()

        # Создаем таблицу, если она еще не существует
        cursor.execute("CREATE TABLE IF NOT EXISTS weather (datetime TEXT, temperature TEXT)")

        # Вставляем данные в таблицу
        cursor.execute("INSERT INTO weather VALUES (?, ?)", (current_datetime, temperature))

        # Получаем данные из таблицы
        cursor.execute("SELECT * FROM weather")
        rows = cursor.fetchall()
        for row in rows:
            print("Дата и время:", row[0])
            print("Температура:", row[1])
            print()

        # Закрываем соединение с базой данных
        conn.close()
    else:
        print("Не удалось найти информацию о температуре на странице погоды.")
else:
    print("Не удалось получить доступ к странице погоды.")

