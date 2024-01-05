import requests
from bs4 import BeautifulSoup


class RequestWeather:
    @staticmethod
    def get_weather(city):
        url = f"https://sinoptik.ua/погода-{city}"
        try:
            response = requests.get(url)
            bs = BeautifulSoup(response.text, "lxml")
            temp = bs.find("p", class_="today-temp").text
            description = bs.find("div", class_="description").text
            return (f"{description}\n"
                    f"Температура: <b>{temp}</b>")
        except AttributeError:
            return f"<b>{city}</b> город не найден, попробуйте ввести иначе: "


