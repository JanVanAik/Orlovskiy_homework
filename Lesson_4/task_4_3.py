from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
content = content.split('</Valute>')


def currency_rates(money_code):
    current_date = content[0].split('Date="')[1][:10]
    for i in content:
        if i.find(money_code.upper()) != -1:
            i = i.split('<Value>')
            return f"Курс к рублю: {float(i[1].replace('</Value>', '').replace(',','.'))} к 1 \n {current_date}"


if __name__ == "__main__":
    user_code = input('Введите код валюты: ')
    print(currency_rates(user_code))
