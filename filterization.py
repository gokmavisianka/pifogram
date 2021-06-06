class Filter:
    def __init__(self):
        self.following = []
        self.followers = []
        self.alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '.']

    def sort_followers(self):
        self.followers = []
        data = open(r"txt_files\followers.txt", "r", encoding="ANSI").read().split('\n')
        self.followers.append(data[2])
        for line in range(len(data)):
            try:
                if data[line] == "Takip Et":
                    self.followers.append(data[line+1])
            except IndexError:
                continue

    def sort_following(self):
        self.following = []
        data = open(r"txt_files\following.txt", "r", encoding="ANSI").read().split('\n')
        self.following.append(data[2])
        for line in range(len(data)):
            try:
                if data[line] == "Takip Et":
                    self.following.append(data[line+1])
            except IndexError:
                continue

        del self.following[0]
        del self.followers[0]

    def write(self):
        try:
            self.sort_followers()
        except IndexError:
            print("Filter.sort_followers() fonksiyonunda hata!")

        try:
            self.sort_following()
        except IndexError:
            print("Filter.sort_following() fonksiyonunda hata!")

        file = open(r"txt_files\followers.txt", "w")
        for person in self.followers:
            file.write(f"{person}\n")
        file.close()

        file = open(r"txt_files\following.txt", "w")
        for person in self.following:
            file.write(f"{person}\n")
        file.close()

