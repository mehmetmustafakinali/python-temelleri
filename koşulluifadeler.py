#koşullu ifadeler 
#if in en büyük aşkı truedir
#karşılaştırma örnekleri 
#eşittir (==) operatörü ile ilgili bir örnek
x = 10
y = 10
if x == y:
    print("x is equal to y.")
print("------------------------------")
#eşit değildir (!=) operatörü ile ilgili bir örnek
x = 10
y = 5
if x != y:
    print("x is not equal to y.")
print("------------------------------")
#büyüktür (>) operatörü ile ilgili bir örnek
x = 10
y = 5
if x > y:
    print("x is greater than y.")
print("------------------------------")
#küçüktür (<) operatörü ile ilgili bir örnek
x = 5
y = 10
if x < y:
    print("x is less than y.")
print("------------------------------")
#büyüktür veya eşittir (>=) operatörü ile ilgili bir örnek
x = 10
y = 10
if x >= y:
    print("x is greater than or equal to y.")
print("------------------------------")
#küçüktür veya eşittir (<=) operatörü ile ilgili bir örnek
x = 5
y = 10
if x <= y:
    print("x is less than or equal to y.")
print("------------------------------")
#kullanıcıdan alınan sayının pozitif, negatif veya sıfır olduğunu kontrol eden bir program
sayi = float(input("Bir sayı girin: "))
if sayi > 0:
    print("Pozitif sayı")
elif sayi < 0:
    print("Negatif sayı")
else:
    print("Sıfır")
print("------------------------------")
#tek satırlık if-else örneği
print("Pozitif sayı") if sayi > 0 else print("Negatif sayı") if sayi < 0 else print("Sıfır")
print("------------------------------")

a = int(input("A sayısını girin: "))
b = int(input("B sayısını girin: "))
if a > b: print(f"{a} büyüktür {b}.")
elif a < b: print(f"{a} küçüktür {b}.")
else: print(f"{a} eşittir {b}.")
#tek satırlık koşullu ifadeler yanlızca çalıştırılacak tek bir satır kod olduğunda kullanılabilir.
#mantıksal operatörlerin koşullu ifadeler ile kullanımı
#and operatörü ile ilgili bir örnek
x = 10
y = 5
if x > 0 and y > 0:
    print("Both x and y are positive.")
print("------------------------------")
#or operatörü ile ilgili bir örnek
x = -10
y = 5
if x < 0 or y < 0:
    print("At least one of x or y is negative.")
print("------------------------------")
#not operatörü ile ilgili bir örnek
x = True
if not x:
    print("x is False.")
print("------------------------------")
#iç içe koşullu ifadeler ile ilgili bir örnek
x = 10
y = 5
if x > 0:
    if y > 0:
        print("Both x and y are positive.")
    else:
        print("x is positive but y is not.")

#boş koşul blokları ile ilgili bir örnek
x = 10
if x > 0:
    pass  # Do nothing
print("------------------------------")
#ellipsis (...) ile boş koşul blokları ile ilgili bir örnek
x = 10
if x > 0:
    ...  # Do nothing
#koşullu ifadeler ile ilgili kapsamlı bir örnek
#vize ve final notuna göre harf notu hesaplama 
vize = float(input("Vize notunu girin: "))
final = float(input("Final notunu girin: "))
avarage = (vize * 0.4) + (final * 0.6)
if avarage >= 90:
    letter_grade = "AA"
elif avarage >= 85:
    letter_grade = "BA"
elif avarage >= 80:
    letter_grade = "BB"
elif avarage >= 75:
    letter_grade = "CB"
elif avarage >= 70:
    letter_grade = "CC"
elif avarage >= 65:
    letter_grade = "DC"
elif avarage >= 60:
    letter_grade = "DD"
else:
    letter_grade = "FF"
print(f"Ortalamanız: {avarage}, Harf Notunuz: {letter_grade}")
print("------------------------------")
#2.örnek kitap sipariş sayısına gör indirim hesaplam 
quantity = int(input("Kaç kitap sipariş etmek istiyorsunuz? "))
book_price = 105.4       # Kitap fiyatı
total_price = quantity * book_price  # Toplam fiyat
if quantity >= 50:
    discount_rate=0.25
elif quantity >= 20:
    discount_rate=0.15
elif quantity >= 10:
    discount_rate=0.10
else:
    discount_rate=0.0
discount_amount = total_price * discount_rate  # İndirim miktarı
final_price = total_price - discount_amount  # İndirimli fiyat
print(f"Toplam fiyat: {total_price}, İndirim miktarı: {discount_amount}, İndirimli fiyat: {final_price}")
print("------------------------------")
#örnek 3:girilen sayının karekökünün tam sayı olup olmadığını kontrol eden bir program
import math
number = int(input("Bir sayı girin: "))
sqrt_number = math.sqrt(number)
if sqrt_number == int(sqrt_number):
    print(f"{number} sayısının karekökü tam sayıdır: {int(sqrt_number)}")
else:
    print(f"{number} sayısının karekökü tam sayı değildir.")
print("------------------------------")
#örnek 4 : GSM operatörlerü aşım faturası hesaplama algoritması
fixed_fee = 50.0  # Sabit ücret
free_minutes = 100  # Ücretsiz dakika
extra_minute_fee = 0.25  # Ekstra dakika ücreti

