import random
import os  
class bilgi():
    def __init__(self,ipucu):
        self.ipucu = ipucu
    def cagir(self):
        print(f"{self.ipucu}")
kalem = bilgi("kagida yazi yazar mektuplar cevaplarım")
ruj = bilgi("dudağa bir renk veririm")
parfum = bilgi("sıkarsan kokarım sıkmazsan kokarsın")
sise = bilgi("sıvı koyulabilir içime")
buz = bilgi("katıyımdır oldukça bakma su olduğuma")
cuzdan = bilgi("kartların ve paran var bende")
vantilator = bilgi("hava sıcaksa çalıştır")
sapka = bilgi("takarsın kafana güneşi engellerim")
kulaklik = bilgi("kulağında çalarım müzik")
cetvel = bilgi("uzunluk ölçerim çok büyük olmaz")
bicak = bilgi("keserim meyve sebze")
kagit = bilgi("yazarsın üstüme yazı") 
kategori = ["kalem","ruj","parfüm","buz","cüzdan","vantilatör","şapka","kulaklık","cetvel","bıçak","kağıt"]
ipucları = [kalem,ruj,parfum,buz,cuzdan,sapka,kulaklik,cetvel,bicak,kagit]
dogruH = []#kullanicidan alinan harfler
yanlisH = []# kullanicidan alinan yanlis harfler
bayrak = True
hak = 7
while bayrak:
    kelime = random.choice(kategori)
    print(kelime)
    kelimeuzun = ["-" * len(kelime)]
    print(kelimeuzun)
    tahmin = input("tahmininiz = ")
    if tahmin == kelime:
        print("tebrikler doğru bildiniz tekrar oynamak istermisiniz e\h")
        eved = input()
        if eved == "e":
            bayrak = True
        else:
            exit()
    if tahmin in kelime:
        kelimeuzun[kelime[tahmin]] = tahmin
        dogruH.append(tahmin)
        print(dogruH)
        print("dogru tahmin yaptiniz")