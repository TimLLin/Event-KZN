import requests
import urllib.request
from bs4 import BeautifulSoup


token_a = '1844668199:AAGqVvqCfa5a60vcEQ_Cm9dNMtuvRslDAXg'
token_t = '1777347114:AAEow6W4NmD1r6OYCmKCtjMRth7olY9hOHk'

querydata = None
event_index = 0
counter_update_photo = 0
message_photo_id = None
url_data = ['https://www.afisha.ru/kazan/schedule_concert/s-biletami/',
            'https://www.afisha.ru/kazan/schedule_exhibition/',
            'https://www.afisha.ru/kazan/schedule_theatre/']
url_querry = None
dic1 = {}
def bulka(url):
    muk = []
    duk = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    suska = soup.find_all('a', class_="_1F19s")
    kek = soup.find_all('a', class_='_1F19s')
    for data in suska:
        if soup.find_all('a', href=True) or soup.find_all('h3', class_='heHLK'):
            muk.append(data.text)
            duk.append('https://www.afisha.ru' + data['href'])
    dic = {key:value for key,value in zip(muk,duk)}
    return dic



def chosen_concert(url):
    muk = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    adress = soup.find_all('div', class_="unit__col unit__col_oneandhalf")
    date = soup.find_all('h2', class_='_2YgOJ')
    slogan = soup.find_all('h2', class_='info-widget__header')
    name = soup.find_all('div', class_="_3kkV1 dbGiX")
    image = soup.find_all('img', class_='EVCML')
    for data in name:
        if soup.find_all('div', class_='_3kkV1 dbGiX'):
            muk.append(data.text)
    for data in slogan:
        if soup.find_all('h2', class_='info-widget__header'):
            delet = []
            delet.append(data.text)
            new_list = [word for line in delet for word in line.split()]
            mes = " ".join(new_list)
            muk.append(mes)
    for data in adress:
        if soup.find_all('div', class_='unit__col unit__col_oneandhalf'):
            muk.append(data.text)
    for data in date:
        if soup.find_all('h2', class_='_2YgOJ'):
            muk.append(data.text)
    message = None
    if url_querry == "https://www.afisha.ru/kazan/schedule_concert/s-biletami/":
        if len(muk)==4:
            message ="Концерт\n\n{}\n\n{}\n\n{}\n{}""".format(muk[0],muk[1],muk[2],muk[3])
        elif len(muk)==3:
            message = "Концерт\n\n{}\n\n{}\n{}".format(muk[0],muk[1],muk[2])
    if url_querry == "https://www.afisha.ru/kazan/schedule_exhibition/":
        message = "Выставка\n\n{}\n\n{}\n\n{}".format(muk[0],muk[1],muk[2])
    if url_querry == "https://www.afisha.ru/kazan/schedule_theatre/":
        adress1 = soup.find_all('div', class_="_1kyNY")
        date = soup.find_all('h2', class_='_2YgOJ')
        desc = soup.find_all('h2', class_='_3X26C')
        shit = soup.find_all('div', class_='_3bJX-')
        for data in date:
            if soup.find_all('div', class_='_1kyNY'):
                muk.append(data.text)
        for data in adress1:
            if soup.find_all('h2', class_='_2YgOJ'):
                muk.append(data.text)
        for data in desc:
            if soup.find_all('h2', class_='_3X26C'):
                muk.append(data.text)
        message = "Спектакаль\n" + "\n\n".join(muk)
    return message

def chosen_theatre(url):
    muk = []
    response = requests.get('https://www.afisha.ru/performance/66800/')
    soup = BeautifulSoup(response.content, 'html.parser')
    adress1 = soup.find_all('div', class_="_1kyNY")
    date = soup.find_all('h2', class_='_2YgOJ')
    desc = soup.find_all('h2', class_='_3X26C')
    shit = soup.find_all('div', class_='_3bJX-')
    for data in date:
        if soup.find_all('div', class_='_1kyNY'):
            muk.append(data.text)
    for data in adress1:
        if soup.find_all('h2', class_='_2YgOJ'):
            muk.append(data.text)
    for data in desc:
        if soup.find_all('h2', class_='_3X26C'):
            muk.append(data.text)
    print(muk)

def chosen_photo(url):
    muk = None
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    image = soup.find_all('img', class_='EVCML')
    for data in image:
        muk = data['src']
    img = urllib.request.urlopen(muk).read()
    out = open("img.jpg", "wb")
    out.write(img)
    return out

chosen_theatre('https://www.afisha.ru/performance/82371/')