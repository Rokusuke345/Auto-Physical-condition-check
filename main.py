from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pickle
from time import sleep
import random
import schedule

def enter(browser):
    for i in range(1,10):
        browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div["+str(i*2)+"]/span/div[3]/div/div").click()
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div").click()
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div").click()
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div").click()
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[3]/div/div/div").click()
    sleep(10)
    #36度
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div").click()
    #35度
    #browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div").click()
    #1:.0,10:.9 default 36.2~36.5
    param = random.randint(3,6)
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[3]/div/div[2]/div/span/div/div["+str(param)+"]/label/div/div[1]/div").click()
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[2]/label/div/div[1]/div").click()
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div/div/div[3]/div/div/div[2]").click()
    sleep(10)
    return

def login(user_data,browser):
    sleep(10)
    #メールアドレス入力
    browser.find_element_by_name("identifier").send_keys(user_data[0])
    browser.find_element_by_xpath("//*[@id='identifierNext']/div").click()
    sleep(20)
    #パスワード入力
    browser.find_element_by_name("password").send_keys(user_data[1])
    browser.find_element_by_xpath("//*[@id='passwordNext']/div").click()
    sleep(20)
    return

def main():
    #コメント解除するとヘッドレス化できると思う。テストしてないので要注意
    '''
    option = Options()
    option.add_argument('--headless')
    browser = webdriver.Chrome(options=option)
    '''
    browser =  webdriver.Chrome()
    browser.get('https://forms.gle/fJhEx3GnEYMaa2xFA')
    try:
        with open('config.txt',mode='rb') as fi:
            data = pickle.load(fi)
    except:
        return
    user_data = data["user"]
    login(user_data,browser)
    enter(browser)
    browser.close()
    print("[+]Process success")
    return
if __name__ == "__main__":
    try:
        with open('config.txt',mode='rb') as fi:
            data = pickle.load(fi)
        time = data["time"]
    except:
        time = "10:00"
    try:
        schedule.every().day.at(time).do(main)
    except:
        print("[-]Process failed")
    while True:
        schedule.run_pending()
    sleep(1)
