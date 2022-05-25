import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

import requests
from bs4 import BeautifulSoup


url = "https://www.iban.com/currency-codes"

print("Bem-vindo ao Negociador de Moeda \nEscolha pelo número da lista o país que deseja consultar o código da moeda\n")


url_moedas = url
r_moedas = requests.get(url_moedas)
html_moedas = r_moedas.text
soup_moedas = BeautifulSoup(html_moedas, 'html.parser')
tds = soup_moedas.find('tbody').find_all('tr')
td_list = []

for td in tds:
    if td.contents[5].get_text() != '':
        moeda_list = {
            'country': td.contents[1].get_text(),
            'currency': td.contents[3].get_text(),
            'code': td.contents[5].get_text(),
            'number': td.contents[7].get_text()
        }
        td_list.append(moeda_list)


def menu():
    try:
        c_moeda_1 = int(input("Informe o número do primeiro país: "))
        c_moeda_2 = int(input("Informe o número do segundo país: "))
        mount = int(input("Informe o valor a ser convertido: "))
        if c_moeda_1 > len(td_list):
            if c_moeda_2 > len(td_list):
                print("Número informado não está na lista")
                menu()
            elif mount == str:
                print("Esse valor não é um número")
                menu()
        else:
            country_1 = td_list[c_moeda_1]
            country_2 = td_list[c_moeda_2]
            converter(country_1['code'], country_2['code'], mount)
    except:
        print("Esse valor não é um número")
        menu()


def converter(moeda_1, moeda_2, mount):

    moeda1 = moeda_1
    moeda2 = moeda_2
    montante = mount
    url = f'https://wise.com/gb/currency-converter/{moeda1}-to-{moeda2}-rate?amount={montante}'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
    url_transfwewise = 'https://wise.com/gb/currency-converter/'
    r_url = requests.get(
        f"{url_transfwewise}{moeda1}-to-{moeda2}-rate?amount={montante}", headers={'User-Agent': user_agent})
    html_url = r_url.text
    soup = BeautifulSoup(html_url, 'html.parser')
    rate = float(soup.find('span', class_='text-success').string)
    print(rate)

    rate_math = montante * rate
    print(format_currency(rate_math, moeda2))
    format_currency(rate_math, moeda2)


for index, country in enumerate(td_list):
    print(f"{index}->{country['country']}")

menu()
