import time
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
from selenium.webdriver.chrome.options import Options
import requests
from fake_useragent import UserAgent

need_to_find = 'Процессоры'
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(f'https://avito.ru/moskva?q={need_to_find.lower()}')
time.sleep(1)
div_elements = driver.find_elements_by_class_name('iva-item-root-_lk9K')
for div_element in div_elements:
    print(div_element.get_attribute('data-item-id'))
time.sleep(10)
# data = requests.get(f'https://avito.ru/moskva?q={need_to_find.lower()}')
# soup = BeautifulSoup(data.content, 'html.parser')
# print(soup)





# ##main
# names_input = open('whitelist.json', 'rt+')
# try:
#     names_output = open("nicks.txt", 'rt+')
# except:
#     with open("nicks.txt",'xt+'):
#         pass
#     names_output = open("nicks.txt", 'rt+')
# while(1):
#     name = ''
#     name_string = names_input.readline()
#     if name_string == '':
#         break
#     if name_string[7:11] == 'name':
#         name = name_string[15:-2]
#         flag = 0
#         names_output.seek(0)
#         while(1):
#             name_string = names_output.readline()
#             if name_string == '':
#                 break
#             if name in name_string:
#                 flag = 1
#                 break
#         if flag == 0:
#             try:
#                 chrome_options = Options()
#                 # chrome_options.add_argument("--headless")
#                 driver = webdriver.Chrome(chrome_options=chrome_options)
#                 driver.get("https://spea.cc/totem/index.php")
#                 time.sleep(1)
#                 website_entry = driver.find_element_by_id("username0")
#                 time.sleep(1)
#                 website_entry.send_keys(str(name))
#                 time.sleep(1)
#                 website_button = driver.find_element_by_class_name("sub").click()
#                 time.sleep(2)
#                 website_image = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[2]/img')
#                 src = website_image.get_attribute("src")
#                 output_string = 'totems\\' + str(name).lower()
#                 urllib.request.urlretrieve(src, output_string+'.png')
#                 with open(output_string+'.properties', 'wt+') as property_file:
#                     property_file.write('type=item\nitems=totem_of_undying\ntexture='+str(name).lower()+'.png\n'+'nbt.display.Name='+name)
#                 time.sleep(2)
#                 driver.close()
#                 names_output.close()
#                 names_output = open("nicks.txt", 'at+')
#                 names_output.write(name+'\n')
#                 names_output.close()
#                 names_output = open("nicks.txt", 'rt+')
#             except:
#                 pass
            
# names_input.close()
# names_output.close()