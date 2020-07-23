from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from InstagramAPI import InstagramAPI

username = "sugerandspiceeverythingnice"
password = "buch+promotion45"

driver = webdriver.Chrome(executable_path = r"D:\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
sleep(random.uniform(0.5, 2.3))

def login():
    try: 
        user_input = driver.find_element_by_xpath('//*[@name="username"]')
        user_input.send_keys(username)
        sleep(random.uniform(0.5, 2.3))
   
        password_input = driver.find_element_by_xpath('//*[@name="password"]')
        password_input.send_keys(password)
        sleep(random.uniform(0.5, 2.3))
        password_input.send_keys(Keys.ENTER)
        sleep(random.uniform(1.0, 2.3))

        driver.get("https://www.instagram.com/" + username + "/")
        sleep(random.uniform(0.5, 2.3))
        return
    
    except:
        print("Error while logging in")
        return

login()

#als eigenes skript ausgliedern
#andere methode für follow/unfollow und kommentare verwenden
def upload_photo():
    api = InstagramAPI(username, password)
    api.login()  
    photo_path = 'D:/Pictures/Instagram/2.jpg'
    caption = "Another photo"
    api.uploadPhoto(photo=photo_path, caption=caption)
    return

exit()

   



