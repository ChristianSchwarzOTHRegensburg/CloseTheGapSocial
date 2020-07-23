from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import random
from time import sleep

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path = r"D:\Downloads\chromedriver_win32\chromedriver.exe", options=options)
video_url = input("Enter your URL: ")
number_of_views = int(input("How many views do you want? "))
watchtime = int(input("How long should the videos be watched? e.g. enter 30 for 30 seconds "))
print("Realistic Viewer Behavior takes more time, but looks more natural to YouTube")
enable_realistic = int(input("Press 1 to enable realsitic viewer behavior "))
current_number = 0

driver.get(video_url)
actions = ActionChains(driver)#sendet an gesamte Webseite, nicht einzelnes Element
actions.send_keys("k").perform() #starts playing the video
actions.send_keys("m").perform() #mutes the video


def realistic_views():
    actions.send_keys(random.randint(1,9)).perform()
    sleep(random.uniform(2.1,3.5))
    return
    
while(current_number < number_of_views):
    driver.refresh()
    sleep(watchtime + random.uniform(1.5,2.))
    if (enable_realistic == 1):
        realistic_views()
    else:
        pass
    current_number += 1
    

print("Complete. Remember that it takes some time for the view counter to refresh")
