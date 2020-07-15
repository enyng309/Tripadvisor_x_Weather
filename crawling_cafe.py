import pandas as pd
import requests
from bs4 import BeautifulSoup

review_page = [""]
headers = {'User-Agent': 'Mozilla/5.0'}
url_list = list()
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d10325923-Reviews-Mayb_Cafe-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d3869141-Reviews-Starbucks_Jeju_Jungmun-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8743706-Reviews-Cafe_Delmoondo-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8926308-Reviews-Bomnal-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8818282-Reviews-Monsant-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d13127944-Reviews-Antoinette-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d9770412-Reviews-Terarosa_Coffee-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d9204364-Reviews-Yudong_Coffee-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d9338088-Reviews-Pung_Rim_Coffee_Shop-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d7132352-Reviews-Cafe_de_Seoyeon-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d17562975-Reviews-Romance_in_Saekdal-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d9245559-Reviews-Starbucks_Seongsan_Ilchulbong-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8917094-Reviews-Blancrocher-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d9228476-Reviews-Twosome_Place-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d10501078-Reviews-Villa_De_Ato-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d9245951-Reviews-Starbucks_Jeju_Jungmun_DT-Seogwipo_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d9245538-Reviews-Starbucks_Jeju_Nohyeong-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d18662922-Reviews-Cafe_Banana_Hamdok-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8891573-Reviews-Cafe_Gongjakso-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8743728-Reviews-Coffine_Gurunaru_Aewol_Handam_Coastal_Walking_Path-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297885-d8428656-Reviews-Starbucks_Sinjeju_E_Mart-Jeju_Jeju_Island.html')
url_list.append('https://www.tripadvisor.co.kr/Restaurant_Review-g297892-d12222379-Reviews-Cafe_Bluehaus-Seogwipo_Jeju_Island.html')


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
info.to_csv("cafe.csv")
