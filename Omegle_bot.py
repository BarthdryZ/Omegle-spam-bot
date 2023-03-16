from selenium import webdriver
from time import sleep
from random import randint
CI = 'tamil'#Type your common interest here
MSG = ('Hello','Hey','Hi') #Type your texts (as an tuple) that you want to spam
while True:
    driver = webdriver.Chrome(executable_path="C:\\Users\Altech_Archeoscr\Downloads\chromedriver_win32\chromedriver")#provide the local download location of chrome driver (Depreciated but unchanged)
    driver.get('https://www.omegle.com/')
    driver.maximize_window()
    sleep(2)
    loginbtn = driver.find_element("xpath", '/html/body/div[3]/table/tbody/tr[2]/td[1]/div/div/div[1]/input')
    loginbtn.send_keys(CI)
    cli = driver.find_element("xpath", '/html/body/div[3]/table/tbody/tr[2]/td[2]/img')
    cli.click()
    sleep(2)
    agr1 = driver.find_element("xpath", '/html/body/div[7]/div/p[1]/label/input')
    agr1.click()
    agr2 = driver.find_element("xpath", '/html/body/div[7]/div/p[2]/label/input')
    agr2.click()
    agr3 = driver.find_element("xpath", '/html/body/div[7]/div/p[3]/input')
    agr3.click()
    sleep(3)
    lol = driver.find_element("xpath", '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea')
    lol.send_keys(MSG[randint(0,len(MSG)-1)])
    sleep(2)
    zaz=driver.find_element("xpath", '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[3]/div/button')
    zaz.click()
    sleep(3)
    driver.close()
