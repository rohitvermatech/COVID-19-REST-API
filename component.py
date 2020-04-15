from bs4 import BeautifulSoup
import requests


def get_covid():
    url = "https://www.worldometers.info/coronavirus/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    table_data = soup.find("table")

    countries = []
    Dict = {}
    for tr_data in table_data.find_all("tr"):
        temp = []
        for data in tr_data.find_all("td"):
            temp.append(data.text.strip())
        try:
            Dict[temp[0].replace("Total:", "Total").lower()] = {
                "total": temp[1],
                "deaths": temp[3],
                "recovered": temp[5],
                "active": temp[6],
            }
        except:
            continue
        countries.append(temp[0].replace("Total:", "Total").lower())
    return Dict, countries


def country(country_name, Dict, countries):
    if country_name in countries:
        return Dict[country_name]
    else:
        return "no data found"
