from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()
url = "http://web.whatsapp.com"
driver.get(url)
input('Enter anything after scanning QR code')
reply = "Hello, I am Jarvis, Mitesh sir is busy. He Will contact you later."
groups = ["PYTHON WORLD(RMC)", "ATG_Python-Scraping_GRP-1", "TYIT", "MU l BSC- All Branch l 6", "Programming Only 1"]
while True:
    time.sleep(60)
    res = driver.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(res, "lxml")
    contacts = soup.find_all('div', {'class': 'X7YrQ'})
    print(len(contacts))
    # contact_names=soup.find_all()_19RFN _1ovWX
    for contact in contacts:

        contact_name = contact.find('span', {'class': '_19RFN'}).text.replace("\n", "").strip()
        try:
            msg_count = contact.find('span', {'class': 'P6z4j'}).text.replace("\n", "").strip()
        except:
            msg_count = 0
        if int(msg_count) > 0 and contact_name not in groups:
            try:
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact_name))
                user.click()
                msg_box = driver.find_element_by_class_name('_3u328')
                msg_box.send_keys(reply)
                driver.find_element_by_class_name('_3M-N-').click()
            except:
                pass
        print(contact_name, msg_count)
