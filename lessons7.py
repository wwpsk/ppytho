#import urllib.request
from bs4 import BeautifulSoup
import requests
# res_parse_list = []
response = requests.get("https://aif.ru/culture/movie/kakoy_rost_u_svinki_peppy")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find("div", class_="vo_o_text")
    res = soup_list.find("p")
    print(res.text)
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 res_parse_list.append(parse_elem_2)
#
# bitcoin_exchange_rate = res_parse_list[0]
# print(bitcoin_exchange_rate)

#opener = urllib.request.build_opener()
#response = opener.open ("https://httpbin.org/get")
#print(response.read())

#response = requests.get("https://httpbin.org/")
#print(response.content)