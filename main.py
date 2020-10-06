from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pickle
from time import sleep
import random
import schedule

def enter(browser):
    #36度
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()
    sleep(1)
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[4]").click()
    #35度
    #browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]).click()
    _min = 1
    _max = 3
    param = random.randint(_max+3,_max+3)
    sleep(1)
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]").click()
    sleep(1)
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div["+str(param)+"]").click()
    sleep(1)
    browser.find_element_by_xpath("//*[@id='i16']/div[3]/div").click()
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div/div/div/span").click()
    sleep(10)
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div/div/div[2]/span").click()
    sleep(10)
    return


def login(user_data,browser):
    sleep(10)
    #メールアドレス入力
    browser.find_element_by_name("identifier").send_keys(user_data[0])
    browser.find_element_by_xpath("//*[@id='identifierNext']/div").click()
    sleep(10)
    #パスワード入力
    browser.find_element_by_name("password").send_keys(user_data[1])
    browser.find_element_by_xpath("//*[@id='passwordNext']/div").click()
    sleep(10)
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
    '''
    try:
        schedule.every().day.at(time).do(main)
    except:
        print("[-]Process failed")
    while True:
        schedule.run_pending()
    '''
    main()
    sleep(1)
