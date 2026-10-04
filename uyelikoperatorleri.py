#üyelik operatörleri ile ilgili bir örnek
list1 = [1, 2, 3, 4, 5]
if 3 in list1:
    print("3 is in the list.")
if 6 not in list1:
    print("6 is not in the list.")
#içinde var mı diye kontrol eden bir program
user_input = int(input("Enter a number: "))
if user_input in list1:
    print(f"{user_input} is in the list.")
    print("The number is in the list.")
else:
    print(f"{user_input} is not in the list.")
    print("The number is not in the list.")
#not in operatörü ile ilgili bir örnek
#içinde yok mu diye kontrol eden bir program
user_input2 = int(input("Enter another number: "))
if user_input2 not in list1:
    print(f"{user_input2} is not in the list.")
    print("The number is not in the list.")
else:
    print(f"{user_input2} is in the list.")
    print("The number is in the list.")


print("----------------------------------------------")
#bitsel operatörler ile ilgili bir örnek
#bitsel ve (&) operatörü ile ilgili bir örnek
x = 5  # binary: 0101
y = 3  # binary: 0011
z = x & y  # binary: 0001, which is 1 in decimal
print("After bitwise AND, z =", z)
#bitsel veya (|) operatörü ile ilgili bir örnek
x = 5  # binary: 0101  
y = 3  # binary: 0011
z = x | y  # binary: 0111, which is 7 in decimal
print("After bitwise OR, z =", z)
#bitsel özel veya (^) operatörü ile ilgili bir örnek
x = 5  # binary: 0101
y = 3  # binary: 0011
z = x ^ y  # binary: 0110, which is 6 in decimal
print("After bitwise XOR, z =", z)
#sola kaydırma (<<) operatörü ile ilgili bir örnek
x = 5  # binary: 0101
z = x << 1  # binary: 1010, which is 10 in decimal
print("After left shift, z =", z)
#sağa kaydırma (>>) operatörü ile ilgili bir örnek
x = 5  # binary: 0101
z = x >> 1  # binary: 0010, which is 2 in decimal
print("After right shift, z =", z)
#bitsel not (~) operatörü ile ilgili bir örnek
x = 5  # binary: 0101
z = ~x  # binary: 1010, which is -6 in decimal (two's complement)
print("After bitwise NOT, z =", z)

print("----------------------------------------------")

#operatör önelik sırası 
#1. Parantezler ()
#2. Üs alma (**)
#3. Çarpma, Bölme, Modül (%), Tamsayı Bölme (//)
#4. Toplama, Çıkarma (+, -)
#örnek
print(2 + 3 * 4)  # Output: 14
#tuple elemanlarına erişim 
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
#sclicing index aralığı belirlemek 
print(my_tuple[1:4])  # Output: (2, 3, 4)
print(my_tuple[:3])   # Output: (1, 2, 3)
#negatif indexleme
print(my_tuple[-1])  # Output: 5
print(my_tuple[-2])  # Output: 4
#NEGATİVE SCLICING
print(my_tuple[-4:-1])  # Output: (2, 3, 4)
#öge varlık kontrolü
fruits = ("apple", "banana", "cherry")
if "banana" in fruits:
    print("Banana is in the tuple.")
else:
    print("Banana is not in the tuple.")
#tuple birleştirme
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: (1, 2, 3, 4, 5, 6)
#tuple içeriği çoğaltma
cars = ("Ford", "BMW", "Volvo")
cars2 = cars * 2
print(cars2)  # Output: ('Ford', 'BMW', 'Volvo', 'Ford', 'BMW', 'Volvo')
#tuplede veri güncelleme yoktur çünkü tuple immutable bir veri tipidir.
#çözüm yolu vardır liste dönüştürüp güncelleme yapıp tekrar tuple yapabiliriz.
#örnek
drinks = ("water", "juice", "soda")
drinks_list = list(drinks)
drinks_list[1] = "tea"  # Update the second element
drinks = tuple(drinks_list)  # Convert back to tuple
print(drinks)  # Output: ('water', 'tea', 'soda')
#tuple eleman ekleme yoktur çünkü tuple immutable bir veri tipidir.
#çözüm yolu vardır liste dönüştürüp ekleme yapıp tekrar tuple yapabiliriz.
#örnek
drinks = ("water", "juice", "soda")
drinks_list = list(drinks)
drinks_list.append("coffee")  # Add a new element
drinks = tuple(drinks_list)  # Convert back to tuple
print(drinks)  # Output: ('water', 'juice', 'soda', 'coffee')
# += ile tuple birleştirme
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple1 += tuple2  # This creates a new tuple and assigns it to tuple1
print(tuple1)  # Output: (1, 2, 3, 4, 5, 6)
#tek eleman eklemede virgül kullanılır yoksa tuple olarak algılanmaz ve hata verir.
tuple3 = (7,)  # This is a tuple with one element
print(tuple3)  # Output: (7,)
#tuplede eleman silme yoktur çünkü tuple immutable bir veri tipidir.
#çözüm yolu vardır liste dönüştürüp silme yapıp tekrar tuple yapabiliriz.
launges = ("Python", "Java", "C++", "JavaScript")   
launges_list = list(launges)
launges_list.remove("C++")  # Remove an element
launges = tuple(launges_list)  # Convert back to tuple
print(launges)  # Output: ('Python', 'Java', 'JavaScript')
print("-------------------------------")
#paketleme ve paketten çıkarma (unpacking) ile ilgili bir örnek
fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits
print(a)  # Output: apple
print(b)  # Output: banana
print(c)  # Output: cherry
#yıldız asterisk kullanımı ile ilgili bir örnek
fruits = ("apple", "banana", "cherry", "date", "elderberry")
(a, b, *c) = fruits
print(a)  # Output: apple
print(b)  # Output: banana
print(c)  # Output: ['cherry', 'date', 'elderberry']
#for döngüsü ile tuple elemanlarına erişim
all_fruits = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon")
for fruit in all_fruits:
    print(fruit)
#tuple eleman sayısı bulma
print(len(all_fruits))  # Output: 10
#index numarası ile gezinme(range() ve len() fonksiyonu ile)    
for i in range(len(all_fruits)):
    print(f"Index {i}: {all_fruits[i]}")
print("------------------------------")
#while döngüsü ile tuple elemanlarına erişim
i = 0
while i < len(all_fruits):
    print(f"Index {i}: {all_fruits[i]}")
    i += 1
#tuple metoları 
print(all_fruits.count("apple"))  # Output: 1
print(all_fruits.index("cherry"))  # Output: 2
#count metodu: belirtilen bir elemanın tuple içinde kaç kez geçtiğini sayar.
#örnek
my_tuple = (1, 2, 3, 2, 4   , 2, 5)
print(my_tuple.count(2))  # Output: 3
print(my_tuple.index(2))  # Output: 1
#index metodu: belirtilen bir elemanın tuple içindeki ilk konumunu döndürür.
#örnek
my_tuple = (1, 2, 3, 2, 4   , 2, 5)
print(my_tuple.index(2))  # Output: 1
