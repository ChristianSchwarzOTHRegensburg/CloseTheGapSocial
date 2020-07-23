import requests
from time import sleep
import random
import free_proxy

video_url = input("Copy the URL of your Video and paste it here: ")
requests.get(video_url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}


number_of_views = int(input("How many views do you want? "))
current_number = 0

while(current_number < number_of_views):
    #proxy = FreeProxy().get()
    #print("Using: ", proxy)
    requests.get(video_url, headers=headers)
    current_number += 1
    sleep(random.uniform(0.5,1.8))

print("You´ve got  new Views!")
