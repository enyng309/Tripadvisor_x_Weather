import pandas as pd
import requests
from bs4 import BeautifulSoup

review_page = [""]
headers = {'User-Agent': 'Mozilla/5.0'}
url_list = ['https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d13137530-Reviews-Indian_Kitchen-Jeju_Jeju_Island.html', 'https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d12453925-Reviews-Gozip_Dol_Wooluck_Jungmun-Seogwipo_Jeju_Island.html', 'https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d6818458-Reviews-Soul_Kitchen-Seogwipo_Jeju_Island.html', 'https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d8954608-Reviews-Narnia_Restaurant_Cafe-Seogwipo_Jeju_Island.html', 'https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8610476-Reviews-Myeongjin_Jeonbok-Jeju_Jeju_Island.html', 'https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d17696597-Reviews-Boraed_Bakers-Seogwipo_Jeju_Island.html', 'https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d9230927-Reviews-Ujin_Haejangguk-Jeju_Jeju_Island.html', 'https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8647545-Reviews-Bluebird_By_Magpie-Jeju_Jeju_Island.html']
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d4033774-Reviews-Ollae_Guksu-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8492137-Reviews-Macho_Grill-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d17637228-Reviews-Gogi_Stop-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d2293565-Reviews-Sunny_Garden-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d5977096-Reviews-Samdajeong-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d6941986-Reviews-Donato_s-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d9284562-Reviews-Jamae_Guksu-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8743739-Reviews-Donsadon-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d12453844-Reviews-Pasta_Studio_Jeju-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d1140355-Reviews-Bagdad_Cafe-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d3612193-Reviews-Heukdonga_Jeju-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8677841-Reviews-Sushi_Hoshikai-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8331072-Reviews-MODICA-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d9230360-Reviews-Willala-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d18717814-Reviews-Gozip_Dol_Wooluck_Hamdok-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d13943597-Reviews-Aewolian-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d8069855-Reviews-Childonga-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d13549775-Reviews-Le_Chinois-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d7042198-Reviews-Biwon-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d4031924-Reviews-Samsunghyeol_Haemultang-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d5561590-Reviews-Samdae_Guksu_Heogwan-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d9297262-Reviews-Rich_Mango-Jeju_Jeju_Island.html')


rate_list = list()
locate_list = list()
name_list = list()
num_list = list()
for i in range(len(url_list)):
    url = url_list[i]
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")

    rate = soup.find("span", {"class": "r2Cf69qf"}).get_text()
    locate = soup.find("a", {"href": "#MAPVIEW"}).get_text()
    name = soup.find("h1", {"class": "_3a1XQ88S"}).get_text()
    num = soup.find("span", {"class": "_3Wub8auF"}).get_text()
    num = num.replace("건의 리뷰", "")

    rate_list.append(rate)
    locate_list.append(locate)
    name_list.append(name)
    num_list.append(num)

name_df = pd.DataFrame({'Name': name_list})
locate_df = pd.DataFrame({'Locate': locate_list})
rate_df = pd.DataFrame({'Rate': rate_list})
num_df = pd.DataFrame({'review_num': num_list})

info = pd.concat([name_df, locate_df, rate_df, num_df], axis=1)
print(info)
info.to_csv("eatery.csv")
