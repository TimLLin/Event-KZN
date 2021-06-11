import requests
from bs4 import BeautifulSoup


token_a = '1844668199:AAGqVvqCfa5a60vcEQ_Cm9dNMtuvRslDAXg'
token_t = '1777347114:AAEow6W4NmD1r6OYCmKCtjMRth7olY9hOHk'

def bulka():
    muk = []
    duk = []
    response = requests.get('https://www.afisha.ru/kazan/schedule_concert/s-biletami/')
    soup = BeautifulSoup(response.content, 'html.parser')
    suska = soup.find_all('a', class_="_1F19s")
    kek = soup.find_all('a', class_='_1F19s')
    for data in suska:
        if soup.find_all('a', href=True) or soup.find_all('h3', class_='heHLK'):
            muk.append(data.text)
            duk.append(data['href'])
    dic = {key:value for key,value in zip(muk,duk)}
    return dic


def chosen_concert():
    muk = []
    response = requests.get('https://www.afisha.ru/concert/2049288/')
    soup = BeautifulSoup(response.content, 'html.parser')
    adress = soup.find_all('div', class_="unit__col unit__col_oneandhalf")
    date = soup.find_all('h2', class_='_2YgOJ')
    image = soup.find_all('img', class_='EVCML')
    for data in adress:
        if soup.find_all('div', class_='unit__col unit__col_oneandhalf'):
            muk.append(data.text)
    for data in date:
        if soup.find_all('h2', class_='_2YgOJ'):
            muk.append(data.text)
    for data in image:
        muk.append(data['src'])

    return muk


chosen_concert()
bulka()

