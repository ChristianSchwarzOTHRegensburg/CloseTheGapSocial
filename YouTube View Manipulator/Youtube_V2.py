from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
from time import sleep

driver = webdriver.Chrome(executable_path = r"D:\Downloads\chromedriver_win32\chromedriver.exe")
video_url = input("Enter your URL: ")
number_of_views = int(input("How many views do you want? "))
watchtime = int(input("How long should the videos be watched? e.g. enter 30 for 30 seconds "))
current_number = 0
driver.get(video_url)

actions = ActionChains(driver)#sended an gesamte Webseite, nicht einzelnes Element
actions.send_keys("k").perform() #starts playing the video
actions.send_keys("m").perform() #mutes the video


while(current_number < number_of_views):
    driver.refresh()
    sleep(watchtime + random.uniform(0.5,1.8))
    current_number += 1
    

print("Complete. Remember that it takes some time for the view counter to refresh")
