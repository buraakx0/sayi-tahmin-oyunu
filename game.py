import random 
import time

girdi = int(input("Sayı tahmin oyununa hoşgeldiniz!\n\n1) Kolay Seviye\n2) Orta Seviye\n3) Zor Seviye\n\nLütfen bir seçenek giriniz: "))

if girdi == 1:
    print("Oyun başlıyor...")
    time.sleep(2)
    kolay = random.randint(1,10)
    cevap = int(input("1 ile 10 arasında sayıyı tahmin etmeye çalış: "))
    kolay != cevap and print("Tahmininiz yanlış! Doğru cevap: {}".format(kolay))
    kolay == cevap and print("Tahmininiz doğru! Tebrikler.")

elif girdi == 2:
    print("Oyun başlıyor...")
    time.sleep(2)
    orta = random.randint(1,25)
    cevap1 = int(input("1 ile 25 arasında sayıyı tahmin etmeye çalış: "))
    orta != cevap1 and print("Tahmininiz yanlış! Doğru cevap: {}".format(orta))
    orta == cevap1 and print("Tahmininiz doğru! Tebrikler.")

elif girdi == 3:
    print("Oyun başlıyor...")
    time.sleep(2)
    zor = random.randint(1,100)
    cevap2 = int(input("1 ile 100 arasında sayıyı tahmin etmeye çalış: "))
    zor != cevap2 and print("Tahmininiz yanlış! Doğru cevap: {}".format(zor))
    zor == cevap2 and print("Tahmininiz doğru! Tebrikler.")


# python game.py
