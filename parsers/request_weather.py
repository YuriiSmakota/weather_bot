import requests
from bs4 import BeautifulSoup


def get_temp(city):
    url = f"https://sinoptik.ua/погода-{city}"
    try:
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "lxml")
        temp = bs.find("p", class_="today-temp").text
        return f"Температура в городе <b>{city}</b>: <b>{temp}</b>"
    except AttributeError:
        return f"<b>{city}</b> город не найден, попробуйте ввести иначе: "



