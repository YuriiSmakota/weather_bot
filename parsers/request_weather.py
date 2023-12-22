import requests
from bs4 import BeautifulSoup


def get_temp():
    url = f"https://sinoptik.ua/"

    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    temp = bs.find("p", class_="today-temp").text
    return f"Температура в городе <b>{temp}</b>"


