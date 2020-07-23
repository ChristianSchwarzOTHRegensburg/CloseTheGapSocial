from InstagramAPI import InstagramAPI
api = InstagramAPI("sugerandspiceeverythingnice", "buch+promotion45")
api.login()  # login
photo_path = 'D:/Pictures/Instagram/1.jpg'
caption = "Photo of an Elephant"
api.uploadPhoto(photo=photo_path, caption=caption)
