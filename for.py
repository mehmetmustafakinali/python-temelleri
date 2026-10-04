#for yapısı 
#for bir döngü türüdür whileden farklı olarak, belirli bir sayıda tekrarlanacak işlemler için kullanılır.
#for döngüsü, bir iterable (tekrarlanabilir) nesne üzerinde döngü oluşturmak için kullanılır.
#while ile nerdeyse aynı işlemi yapar fakat while döngüsü, belirli bir koşul sağlandığı sürece çalışır ve koşul sağlanmadığında döngü sona erer. For döngüsü ise belirli bir sayıda tekrarlanacak işlemler için kullanılır.
#break ve continue komutları ile birlikte kullanılabilir. break komutu döngüyü sonlandırır, continue komutu ise döngünün bir sonraki iterasyonuna geçer.
#range() fonksiyonu ile birlikte kullanıldığında, belirli bir sayıda tekrarlanacak işlemler için kullanılabilir. range() fonksiyonu, belirli bir aralıkta sayılar üretir ve for döngüsü bu sayılar üzerinde iterasyon yapar.
#for else yapısı ile birlikte kullanıldığında, döngü tamamlandığında else bloğu çalıştırılır. Ancak, break komutu ile döngü sonlandırılırsa else bloğu çalıştırılmaz.
#örnekler:
#for döngüsü ile birlikte range() fonksiyonu kullanımı
for i in range(5):
    print(i)
print("------------------------------")
#for döngüsü ile birlikte range() fonksiyonu kullanımı
for i in range(1, 10, 2):
    print(i)
print("------------------------------")
#for döngüsü ile birlikte iterable bir nesne kullanımı
fruits = ["elma", "armut", "muz", "çilek"]
for fruit in fruits:
    print(fruit)
print("------------------------------")
#for döngüsü ile birlikte break komutu kullanımı
for i in range(5):
    if i == 3:
        break
    print(i)
print("------------------------------")
#for döngüsü ile birlikte continue komutu kullanımı
for i in range(5):
    if i == 3:
        continue
    print(i)
print("------------------------------")
#DETATLI ÖRNEKLER 
#COUNTİNUE KOMUTU İLE İLGİLİ ÖRNEK: KULLLANICIDAN GİRİLEN SAYILARI İLE TEK ÇİFT SAYI ALGORİTMASI
print("------------------------------")
number_list = []
for i in range(5):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
        continue
    else:
        print(f"{number} is odd.")
    number_list.append(number)
    print(f"Current list: {number_list}")
#boş kod bloklarını yönetme: pass deneyim ve üç nokta (...) kullanımı
#pass komutu ile boş kod bloklarını yönetme
print("------------------------------")
#örnek 1
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)
print("------------------------------")
#iç içe döngüler ile ilgili bir örnek
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")
print("------------------------------")
#gerçek hayat örneği öğrenci listetsi iç içe döngü ile yazdırma işlemi
students = ["Ali", "Ayşe", "Mehmet"]
for student in students:
    for i in range(3):
        print(f"{student} is in class {i+1}")
print("------------------------------")
#range kullanmadan for döngüsü ile ilgili bir örnek
print("------------------------------")
mycars = ["bmw", "mercedes", "audi", "volvo"]
for car in mycars:
    print(car)
#daha detaylı bir örnek 
for i, car in enumerate(mycars):
    print(f"Index: {i}, Car: {car}")

print("------------------------------")
fruts = ["elma", "armut", "muz", "çilek"]
for index, item in enumerate(fruts):
    print(f"Index: {index}, Item: {item}")
#zip yerleşik function ile ilgili bir örnek
#zip() fonksiyonu, birden fazla iterable (tekrarlanabilir) nesneyi birleştirerek, her bir öğeyi bir tuple (demet) olarak döndürür. Bu sayede, birden fazla listeyi veya iterable nesneyi aynı anda işleyebiliriz.
#örnek 1
names = ["Ali", "Ayşe", "Mehmet"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")
print("------------------------------")
import random
#python sayı tahmin oyunu 
#özellikler : impoert random , remaining attempts , score ,attemp count for ile yap
random_number = random.randint(1, 100)
remaining_attempts = 5
score = 100
attempt_count = 0
for attempt in range(remaining_attempts):
    user_guess = int(input("Guess a number between 1 and 100: "))
    attempt_count += 1
    if user_guess == random_number:
        print(f"Congratulations! You've guessed the number {random_number} in {attempt_count} attempts.")
        break
    elif user_guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    score -= 20
    print(f"Remaining attempts: {remaining_attempts - attempt}, Current score: {score}")
print(f"The correct number was: {random_number}")
print("------------------------------")
#girilen sayının asal olup olmadoığını bulan program function kullanmadan for döngüsü ile yapın 
number = int(input("Enter a number: "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
print("------------------------------")
#girilen sayıya kadar olan tüm asal sayıları ekrana bastıran ve toplamınıda gösteren programı function kullanmadan yapınız 
prime_numbers = []
number = int(input("Enter a number: "))
for num in range(2, number + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
        print(f"{num} is a prime number.")

print(f"Prime numbers: {prime_numbers}")
print(f"Sum of prime numbers: {sum(prime_numbers)}")





























#iterable bir nesne üzerinde döngü oluşturmak için kullanılır.
#örnek 1
for i in range(5):
    print(i)
#örnek 2
for i in range(1, 10, 2):
    print(i)
#Iterable tekrarlanabilir yapıdadır. Örnek olarak listeler, demetler, sözlükler ve stringler iterable yapılardır.
#örnek 3
fruits = ["elma", "armut", "muz", "çilek"]
for fruit in fruits:
    print(fruit)
