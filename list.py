#listler 
from shutil import copy


liste = [1, 2, 3, 4, 5]
print(liste)
print(liste[0])#ilk eleman
print(liste[-1])#son eleman
print(len(liste))#liste uzunluğu
print(liste[1:4])#2. elemandan 4. elemana kadar
#liste.append(6)#listeye eleman ekleme
liste.append(6)
print(liste)
#listler eklenen eleman listenin sonuna eklenir
#list metodları 
#append() metodu: listenin sonuna bir eleman ekler.
#örnek
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
#insert() metodu: belirtilen bir konuma bir eleman ekler.
cars = ["Ford", "BMW", "Volvo"]
cars.insert(1, "Toyota")
print(cars)  # Output: ['Ford', 'Toyota', 'BMW', 'Volvo']
#remove() metodu: belirtilen bir elemanı listeden kaldırır.
players = ["Messi", "Ronaldo", "Neymar"]
players.remove("Ronaldo")
print(players)  # Output: ['Messi', 'Neymar']
#pop() metodu: belirtilen bir konumdaki elemanı listeden kaldırır ve döndürür.
numbers = [10, 20, 30, 40]
numbers.pop(2)  # Removes the element at index 2 (30)
print(numbers)  # Output: [10, 20, 40]
#clear() metodu: listedeki tüm elemanları kaldırır.
colors = ["red", "green", "blue"]
colors.clear()
print(colors)  # Output: []
#sort() metodu: listedeki elemanları sıralar.
ages = [25, 18, 30, 22]
ages.sort()
print(ages)  # Output: [18, 22, 25, 30]
#reverse() metodu: listedeki elemanların sırasını tersine çevirir.
letters = ["a", "b", "c", "d"]
letters.reverse()
print(letters)  # Output: ['d', 'c', 'b', 'a']
#count() metodu: belirtilen bir elemanın listede kaç kez geçtiğini sayar.
numbers = [10, 20, 30, 40, 30, 50]
count = numbers.count(30)
print(count)  # Output: 2
#extend() metodu: bir listeyi başka bir listeye ekler.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]
#copy() metodu: bir listenin kopyasını oluşturur.
original_list = ["apple", "banana", "cherry"]
copied_list = original_list.copy()
print(copied_list)  # Output: ['apple', 'banana', 'cherry']
#listeler yanlızca tek bir veri tipinden oluşmak zorunda değil 
list=["apple",20,2.6,"banana",True]
#gibi farklı veri tiplerinden oluşabilir
#veri türünü görmek için type() fonksiyonu kullanılır
print(type(list))
#listde genelde [] köşeli parantezler kullanılır
#ancak list() fonksiyonu ile de listeler oluşturulabilir
list3 = list(("apple", "banana", "cherry"))
print(list3)  # Output: ['apple', 'banana', 'cherry']
#arrraylar 4 temel yapıya ayrılır pythonda yani 4 temel koleksiyon vardır
#list, tuple, set ve dictionary
#listler değiştirilebilir,tekrarlanabilir ve sıralıdır
#tuplelar değiştirilemez,tekrarlanabilir ve sıralıdır
#dictionaryler değiştirilebilir,tekrarlanamaz ve sıralı değildir    
#setler değiştirilebilir,tekrarlanamaz ve sıralı değildir
#burada sıradan kastedilen şey elemanların eklenme sırasıdır.daima sona eklenir ve eklenme sırasına göre sıralanır.
#aralık belirterek list elemanlarına  erişmek 
#örnek 
fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
print(fruits[1:4])  # Output: ['banana', 'cherry', 'date']
#banana ile fig arasındaki değerleri getirir bananayı alır ama fig almaz 
#başlangıcı boş bırakma 
print(fruits[:4])  # Output: ['apple', 'banana', 'cherry', 'date']
#bitişi boş bırakma
print(fruits[2:])  # Output: ['cherry', 'date', 'fig', 'grape']
#hepsinin boş bırakırsak bize tüm listi getirir 
print(fruits[:])  # Output: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
#negtif dilimleme 
print(fruits[-4:-1])     # Output: ['cherry', 'date', 'fig', 'grape']
print("----------------------------------------------")
#eleman varlık kontrolü 
solar_system = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
if "Earth" in solar_system:
    print("Earth is in the solar system.")
else:
    print("Earth is not in the solar system.")
#liste eleman değiştirme
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
#belirli bir aralıkta eleman değiştirme
colors = ["red", "green", "blue", "yellow"]
colors[1:3] = ["purple", "orange"]
print(colors)  # Output: ['red', 'purple', 'orange', 'yellow']
#NOT:EĞER ARALIKTAN AZ ÖĞE EKLERSENİZ:
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [10, 20]
print(numbers)  # Output: [1, 10, 20, 5]
#EKLEDĞİNİZ ELEMANLAR BİRDE ONDAN ÖNCEKİ ELEMANLAR KALIR SADECE 
print("----------------------------------------------") 
#+ operatörü ile listeleri birleştirme
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)  # Output: [1, 2, 3, 4, 5, 6]
#iç içe geçmiş listeler 
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0])  # Output: [1, 2, 3]
print(nested_list[1][2])  # Output: 6
#iç içe geçmiş listelerde derin kopyalama
deep_copied_list = copy.deepcopy(nested_list)
print(deep_copied_list)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#del anahtar kelimesi ile listeden eleman silme
del nested_list[1]
print(nested_list)  # Output: [[1, 2, 3], [7, 8, 9]]
#clear()  metodu ile del arasındaki fark biri sadece içini siler diğeri direkt ramdan siler 
nested_list.clear()
#index metodu
cars = ["Ford", "BMW", "Volvo"]
idx=cars.index("BMW")
print(idx)  # Output: 1
print("----------------------------------------------")
#SORT METODU İLE ALFA NUMERİK SIRALAMA
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']
#burada bir nüans var büyük harfler küçük harflerden önce gelir ve sıralama buna göre yapılır
#bunu kırmanın bir yolu var olan sort metoduna key parametresi vermektir ve bu parametreye str.lower fonksiyonunu verirsek büyük küçük harf ayrımı yapmadan sıralama yapabiliriz
fruits = ["banana", "Apple", "cherry"]
fruits.sort(key=str.lower)
print(fruits)  # Output: ['Apple', 'banana', 'cherry']
#z den a ya sıralama yapmak için reverse parametresini True yapmamız gerekir
fruits = ["banana", "apple", "cherry"]
fruits.sort(reverse=True)
print(fruits)  # Output: ['cherry', 'banana', 'apple']
print("----------------------------------------------")
#özel fonksiyonlar ile sıralama 
def custom_sort(item):
    return len(item)  # Sort by the length of the string
fruits = ["banana", "apple", "cherry", "kiwi"]
fruits.sort(key=custom_sort)
print(fruits)  # Output: ['kiwi', 'apple', 'banana', 'cherry']
