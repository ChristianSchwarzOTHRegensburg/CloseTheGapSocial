from time import sleep
import random
from InstagramAPI import InstagramAPI
from PIL import Image
import glob
import os
import shutil

username = "sugerandspiceeverythingnice"
password = "buch+promotion45"
image_list = []

for filename in glob.glob('D:/Pictures/Instagram/*.jpg'): 
    im=Image.open(filename)
    image_list.append(im)

#print(image_list)
#os.replace("D:/Pictures/Instagram/2.jpg", "Desktop/2.jpg")
shutil.move("D:/Pictures/Instagram/2.jpg", "Desktop/2.jpg")

def upload_photo():
    api = InstagramAPI(username, password)
    api.login()  
    photo_path = 'D:/Pictures/Instagram/2.jpg'
    caption = "Another photo"
    api.uploadPhoto(photo=photo_path, caption=caption)
    return

exit()

   




