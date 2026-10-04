#while döngüleri 
#sonsuz döngüde olabilir buna dikkat etmek gerekir 
"""while True:
    print("python")"""
#bu döngü orası false olana kadar devam eder ama bu kodda false olmadığı için sonsuz döngüye girer 
#sonsuz döngüyü önlemek için şayaç değişkeni ve döngü sonlandırma gibbi şeyler kullanılır
i = 0
while i < 5:
    print(i, "python")
    i += 1
#burada i değişkeni 5 olana kadar devam et der ama 5 olmayacak 
print("------------------------------")
#GERİYE DOĞRU SAYAN DÖNGÜ ÖRNEĞİ 
i = 7 
while i > 0:
    print(i, end=" ")
    i -= 1
#print içine end kullanıması alt satıra geçmesini engellemek ve yan yana yazmasını sağlar
print("\n------------------------------")
#break komutu 
i = 1 
while i <= 7:
    print(i)
    if i == 4:
        break
    i += 1
#burada i 4 olursa döngüyüyü kır çık diyor o yüzden arttıramaz.
print("------------------------------")
#countinue komutu
i = 1
while i < 5 : 
    i += 1
    if i == 3 : 
        continue
    print(i)
#BREAKLA COUNTINUE ARASINDAKİ FARK: BREAK DİREKT KIRIP ÇIKAR CONTINUE İSE O ANKİ İŞLEMİ ATLAYIP DÖNGÜYE DEVAM EDER. 
print("------------------------------")
#countinue kullanımında sonsuz döngü riskine dikkat etmek gerekir çünkü continue komutu döngüye devam etmesini sağlar ve i değişkeni arttırılmazsa sonsuz döngüye girer.
"""i = 7 
while i > 0:
    if i == 4:
        continue
    print(i)
    i -= 1"""
#DOĞRU KULLANIMI
i = 7
while i > 0:
    if i == 4:
        i -= 1
        continue
    print(i)
    i -= 1
print("------------------------------")
#PYTHON ÖZEL WHİLE ELSE KULLANIMI
i = 1 
while i <= 7:
    print(i)
    i +=1
else:
    print("döngü bitti")
#listler ve while döngüsü
fruits = ["elma", "armut", "muz", "çilek"]
i = 0 
while i < len(fruits):
    print(fruits[i],end=" ")
    i += 1
print("\n------------------------------")

#birden kullanıcının girdiği sayıya kadar olan sayıların toplamını bulan program
sayi = int(input("bir sayi giriniz:"))
toplam = 0
i = 1 
while i <= sayi:
    toplam += i
    i += 1
print("1'den",sayi,"kadar olan sayıların toplamı:",toplam)

print("------------------------------")
#kullanıcıdan alınan ayıları listeye alma sırlama , toplama ve ekrana yazdırma işlemleri
my_numbers = []
i = 0
while i < 7: 
    sayi = int(input("bir sayi giriniz:"))
    my_numbers.append(sayi)
    i += 1 
    toplam += sayi
print("girilen sayılar:",my_numbers)
print("girilen sayıların toplamı:",toplam)
print("*------------------------------")
#başlangıç ve bitiş değerleri arasındaki tek ve çift sayıları ekrana yazdırma işlemleri
baslangic = int(input("başlangıç değerini giriniz:"))
bitis = int(input("bitiş değerini giriniz:"))
i = baslangic
while i < bitis:
    if i % 2 == 0:
        print(i,"çift sayıdır")
    else:
        print(i,"tek sayıdır")
    i += 1
#NOT NERDE ÇOKLULUK VARSA ORADA DÖNGÜ KULLANILIR.
print("------------------------------")
#kullanıcıdan geçerli isim alma ve boş girdi girdiyi engelleme işlemleri
isim = input("bir isim giriniz:")
while isim == "":
    print("geçerli bir isim giriniz")
    isim = input("bir isim giriniz:")
print("geçerli bir isim girdiniz:",isim)
print("------------------------------")
#bir sayının faktoriyelini hesaplayan program
sayi = int(input("bir sayı giriniz:"))
faktoriyel = 1
i = 1
while i <= sayi:
    faktoriyel *= i
    i += 1
print(sayi,"sayısının faktoriyeli:",faktoriyel)
print("------------------------------")
#BİTTİ