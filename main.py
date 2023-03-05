from bs4 import BeautifulSoup
import requests
response = requests.get("https://finance.ua/ua/banks/oschadbank/currency")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td", {"class" : "heading-block-currency-rate__table-col"})
    res = soup_list[10]
b = float(res.text)
print(b)