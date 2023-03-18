import random
import time

baslangic = time.time()
min, max, sayac = 0, 100, 0
sayi = random.randint(min, max)

print(f"Rastgele sayı: {sayi}")

while True:
    number = random.randint(min, max)
    if number < sayi:
        print(f"{number} değerinden daha büyük bir sayı tahmin ediniz", (number, max))
        min = number
        sayac += 1
    elif number > sayi:
        print(f"{number} değerinden daha küçük bir sayı tahmin ediniz", (number, max))
        max = number
        sayac += 1
    else:
        print(f"{number} tahmininizi {sayac} denemede doğru bildiniz", (number, max))
        break

bitis = time.time()
sonuc = bitis - baslangic
print("Bu işlemde  geçen süre {}".format(sonuc))