import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from filterization import Filter


class Instagram:
    def __init__(self, user):
        self.user = user
        self.id, self.password = None, None
        self.followers = []
        self.following = []
        self.instagram_link = "https://www.instagram.com/" + self.user

    def start_driver(self):
        print("Driver başlatılıyor...")
        op = webdriver.ChromeOptions()
        op.headless = False
        self.driver = webdriver.Chrome(r'driver\chromedriver.exe', options=op)

        self.ac = ActionChains(self.driver)
        self.delay(3)

    def go_to_instagram(self):
        print("Instagram'a giriliyor...")
        self.driver.get("https://www.instagram.com/")
        self.delay(1)

    def login(self):
        data = open(r"txt_files\acc_info.txt", "r").read().split("\n")
        self.id, self.password = data[0][4:], data[1][4:]
        print("Kullanıcı adı giriliyor...")
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.id)
        self.delay(1)
        print("Şifre giriliyor...")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        self.delay(1)
        print("'Giriş Yap' butonuna basılıyor...")
        self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
        self.delay(4)
        print("Ara sekme geçiliyor...")
        try:
            self.driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
        except:
            print("Beklenen ara sekme ile karşılaşılmadı?! İşleme devam ediliyor...")
        self.delay(1)
        self.driver.get(self.instagram_link)
        self.delay(1)
        print(f"{self.instagram_link} sekmesine ulaşıldı!")

    def get_followers_and_following(self):
        print(f"{self.user} isimli kullanıcıyı takip edenlerin listesi alınıyor...")
        self.driver.find_element(By.XPATH, f'//a[@href="/{self.user}/followers/"]').click()
        self.delay(4)
        sayac = 0
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a').send_keys(
            Keys.PAGE_DOWN)

        self.delay(2)

        element = self.driver.find_element(By.XPATH,
                                 '/html/body/div[5]/div/div/div[2]/ul/div/li[5]/div/div[2]/button')
        while True:
            followers_sc = self.driver.find_element(By.XPATH, '//div[@class="isgrP"]')
            followers_text = followers_sc.text
            followers_count1 = len(followers_text.split())
            for n in range(40):
                element.send_keys(Keys.PAGE_DOWN)
            followers_sc = self.driver.find_element(By.XPATH, '//div[@class="isgrP"]')
            followers_text = followers_sc.text
            followers_count2 = len(followers_text.split())
            if followers_count1 == followers_count2:
                sayac += 1
                if sayac == 2:
                    open(r"txt_files\followers.txt", "w", encoding="UTF-8").write(followers_text)
                    print("Takipçilerin listesi alınarak followers.txt'ye başarıyla kaydedildi.")
                    break
            else:
                sayac = 0

        self.delay(2)
        self.driver.get(self.instagram_link)
        print("Sekmeye tekrardan ulaşılıyor...")
        self.delay(2)

        print(f"{self.user} isimli kullanıcının takip ettiklerinin listesi alınıyor...")
        self.driver.find_element(By.XPATH, f'//a[@href="/{self.user}/following/"]').click()
        self.delay(2)
        sayac = 0
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a').send_keys(
            Keys.PAGE_DOWN)
        self.delay(4)
        element = self.driver.find_element(By.XPATH,
                                 '/html/body/div[5]/div/div/div[2]/ul/div/li[5]/div/div[2]/button')
        self.delay(2)
        while True:
            following_sc = self.driver.find_element(By.XPATH, '//div[@class="isgrP"]')
            following_text = following_sc.text
            following_count1 = len(following_text.split())
            for n in range(40):
                element.send_keys(Keys.PAGE_DOWN)
            following_sc = self.driver.find_element(By.XPATH, '//div[@class="isgrP"]')
            following_text = following_sc.text
            following_count2 = len(following_text.split())
            if following_count1 == following_count2:
                sayac += 1
                if sayac == 2:
                    open(r"txt_files\following.txt", "w", encoding="UTF-8").write(following_text)
                    print("Takipçilerin listesi alınarak following.txt'ye başarıyla kaydedildi.")
                    break
            else:
                sayac = 0

    def delay(self, seconds):
        if seconds <= 0:
            raise ValueError(f"Delay fonksiyonunun parametresi 0'dan büyük olmalıdır. Girilen değer: {seconds}")
        elif seconds == 1:
            time.sleep(1)
        else:
            print(f"{seconds} saniyelik gecikme bekleniyor.")
            for second in range(seconds, 0, -1):
                print(f"{second}...", end="")
                time.sleep(1)
            print("0...\n")

    def save_all_info(self):
        file = open(r"txt_files\instagram_info.txt", "w")
        file.write("//////////////////////////////////////////////////////////\n")

        line = 0
        for person in self.following:
            if self.followers.count(person) == 0:
                file.write(f"{line}: {person} isimli kullanici seni takip etmiyor.\n")
                line += 1

        file.write("//////////////////////////////////////////////////////////\n")

        line = 0
        for person in self.followers:
            if self.following.count(person) == 0:
                file.write(f"{line}: {person} isimli kullaniciyi takip etmiyorsun.\n")
                line += 1

        file.write("//////////////////////////////////////////////////////////\n")

    def update(self):
        self.followers = open(r"txt_files\followers.txt", "r").read().split("\n")
        self.following = open(r"txt_files\following.txt", "r").read().split("\n")

    def quit(self):
        self.driver.quit()
