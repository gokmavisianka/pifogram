import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from instagram_bot import *

# ---------------------------------------------------------------------- #
Instagram = Instagram(input("Verileri çekmek istediğiniz Instagram kullanıcısının adını giriniz: "))

Filter = Filter()
Instagram.start_driver()
Instagram.go_to_instagram()
Instagram.login()

Instagram.get_followers_and_following()
Filter.write()
Instagram.update()
Instagram.save_all_info()
print("Görev başarıyla tamamlandı! Çıkış yapılıyor...")
Instagram.delay(2)
Instagram.quit()

# ---------------------------------------------------------------------- #