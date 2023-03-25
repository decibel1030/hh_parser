import json

from bs4 import BeautifulSoup
import requests
import lxml
from fake_useragent import UserAgent
import random


def get_vac_list():
    ua = UserAgent()
    res = requests.get("https://api.hh.ru/vacancies?text=python&area=40&search_period=1&order_by=publication_time",
                       headers={"user-agent": ua.random}).json()
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(res, file, indent=2, ensure_ascii=False)

    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_data():
    data = get_vac_list()
    vac_list = []
    for i in data["items"]:
        if i["salary"]:
            if i["salary"]["from"] is not None:
                sol = f"{i['salary']['from']}-{i['salary']['to']}{i['salary']['currency']}"
            else:
                sol = f"{i['salary']['to']}{i['salary']['currency']}"
        else:
            sol = "з/п не указана"
        vac_list.append({
            "name": i["name"],
            "area": i["area"]["name"],
            "status": i["type"]["name"],
            "link": f"https://hh.kz/vacancy/{i['id']}?"
                    f"query=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&"
                    f"from=vacancy_search_list",
            "employer-name": i["employer"]["name"],
            "role": i["professional_roles"][0]["name"],
            "sol": sol,
            "requirements": i["snippet"]["requirement"]
        })

    return vac_list


def rewrite_data():
    ua = UserAgent()
    res = requests.get("https://api.hh.ru/vacancies?text=python&area=40&search_period=1&order_by=publication_time",
                       headers={"user-agent": ua.random}).json()
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(res, file, indent=2, ensure_ascii=False)


for item in get_data():
    print(item["requirements"] + "\n")