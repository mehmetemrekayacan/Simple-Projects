import time
list_even=[]
list_odd=[]
while True:
    x=int(input("sayı giriniz: "))
    if x % 2 == 0:
        list_even.append(x)
    elif x % 2 != 0:
        list_odd.append(x)
    y = input("sayı girmeye devam etmek istersen 'Entera' bas ya da 'hayır' diyip çık")
    if y=="hayır" or y=="HAYIR":
        print("sistemden çıkılıyor...")
        time.sleep(1)
        break
print("çift sayı sayısı: ",len(list_even),list_even)
print("tek sayı sayısı: ",len(list_odd),list_odd)