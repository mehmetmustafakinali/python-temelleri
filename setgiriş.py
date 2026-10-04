#set veri türü 
#set, elemanları benzersiz ve sıralı olmayan bir veri türüdür.
my_set = {1, 2, 3, 4, 5}
print(my_set)
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)
print("-------------------------------")
#set yapıcı fonksiyonu ile set oluşturma
my_set2 = set([1, 2, 3, 4, 5])
print(my_set2)
print("-------------------------------")
#type fonksiyonu ile veri tipini öğrenme
print(type(my_set2))
print("-------------------------------")
#tekrarlı veri davranışı
my_set3 = {1, 2, 2, 3, 3, 4, 4, 5, 5}
print(my_set3)
print("-------------------------------")
#boolen çakışması
my_set4 = {True, False, 1, 0}
print(my_set4)
print("-------------------------------")
#len fonksiyonu ile set eleman sayısı bulma
print(len(my_set4))
print("-------------------------------")
#veri tip esnekliği: tuple içinde hem metin hemde sayısal değerler olabilir
my_mixed_tuple = ("apple", 1, "banana", 2, "cherry", 3)
print(my_mixed_tuple)
print("-------------------------------")
#set elemanlarına erişim ve arama işlemleri
my_set = {1, 2, 3, 4, 5}
print(my_set)
print("-------------------------------")
#set elemanlarına erişim
books = {"The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice"}
for book in books:
    print(book)
print("-------------------------------")
#üyelik testleri
print("The Great Gatsby" in books)  # Output: True
print("The Catcher in the Rye" in books)  # Output: False
print("The Catcher in the Rye" not in books)  # Output: True
print("-------------------------------")
#python koleksiyon türleri kaşılaştırması özet tablosu : 
print("Python Koleksiyon Türleri Karşılaştırması:")
print("Set: Elemanları benzersiz ve sıralı olmayan bir veri türüdür.")
print("List: Elemanları sıralı ve değiştirilebilir bir veri türüdür.")
print("Tuple: Elemanları sıralı ve değiştirilebilir olmayan bir veri türüdür.")
print("Dictionary: Anahtar-değer çiftlerinden oluşan bir veri türüdür.")
print("Setler, listeler ve tuple'lar sıralı veri türleridir, ancak setler benzersiz elemanlar içerir ve sıralı değildir.")
print("Listeler değiştirilebilir, tuple'lar değiştirilemez ve dictionary'ler anahtar-değer çiftlerinden oluşur.")
print("Setler, listeler ve tuple'lar sıralı veri türleridir, ancak setler benzersiz elemanlar içerir ve sıralı değildir.")
print("Listeler değiştirilebilir, tuple'lar değiştirilemez ve dictionary'ler anahtar-değer çiftlerinden oluşur.")
print("-------------------------------")
print("-------------------------------")
#set verilerine ekleme ve birleştirme işlemleri 
universities = {"Harvard", "MIT", "Stanford", "Oxford", "Cambridge", "Yale", "Princeton", "Columbia", "Caltech", "UCLA", "UC Berkeley", "University of Chicago", "University of Pennsylvania", "Cornell", "Duke", "Johns Hopkins", "Northwestern", "University of Michigan", "University of California, San Diego", "University of Washington"}
universities.add("University of Toronto")
universities.add("University of Melbourne")
print("-------------------------------")
#update() metodu ile birden fazla eleman ekleme
universities.update(["University of Sydney", "University of Auckland", "University of Edinburgh"])
print("-------------------------------")
#pipeline (|) operatörü ile set birleştirme
other_universities = {"University of Melbourne", "University of Sydney", "University of Auckland", "University of Edinburgh"}
combined_universities = universities | other_universities
print("-------------------------------")
print(combined_universities)
#tekrarlı verileri engellemek ve küme birleşimi 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
combined_set = set1 | set2
print(combined_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("-------------------------------")
#setde remove() ve discard() metotları ile eleman silme işlemleri
universities.remove("University of Toronto")
universities.discard("University of Melbourne")
#discard() metodu, silmek istediğiniz eleman set içinde yoksa hata vermez, remove() metodu ise hata verir.
print("-------------------------------")
#pop() metodu ile rastgele eleman silme işlemi
universities.pop()
print("-------------------------------")
#clear() metodu ile tüm elemanları silme işlemi
universities.clear()
#del anahtar kelimesi ile seti tamamen silme işlemi
del universities
print("-------------------------------")
#küme birleşimi, kesişimi ve farkı işlemleri
#ünion() metodu ile küme birleşimi
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union_set = set_a.union(set_b)
print("-------------------------------")
#tuple ve listelerde de union() metodu kullanılabilir ama setlerde daha çok kullanılır çünkü setler benzersiz elemanlar içerir.
#çoklu kullanımı 
set_c = {7, 8, 9, 10}
set_d = {10, 11, 12, 13}
print("-------------------------------")
union_set = set_a.union(set_b, set_c, set_d)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("-------------------------------")
#update() metodu ile küme birleşimi
set_a.update(set_b)
print("-------------------------------")
#pipe sadece set veri türünde çalışır, list ve tuple veri türlerinde çalışmaz.
print(set_a)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}    
print("-------------------------------")
print("küme kesişimi ve farkı işlemleri")
print("-------------------------------")
#intersection() metodu ile küme kesişimi
book_set1 = {"The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice"}
book_set2 = {"1984", "Pride and Prejudice", "The Catcher in the Rye", "The Hobbit"}
intersection_set = book_set1.intersection(book_set2)
print(intersection_set)  # Output: {'1984', 'Pride and Prejudice'}
launges = {"Python", "Java", "C++", "JavaScript"}
launges2 = ["Java", "C#", "Ruby", "Python"]
print("-------------------------------")
intersection_set2 = launges.intersection(launges2)
#ampersand (&) operatörü ile küme kesişimi
intersection_set3 = book_set1 & book_set2
print(intersection_set3)  # Output: {'1984', 'Pride and Prejudice'}
print(intersection_set2)  # Output: {'Python', 'Java'}
#& operatörü sadece set veri türünde çalışır, list ve tuple veri türlerinde çalışmaz.
#intersection_update() metodu ile küme kesişimi
book_set1.intersection_update(book_set2)
#&= operatörü ile küme kesişimi
book_set1 &= book_set2
print(book_set1)  # Output: {'1984', 'Pride and Prejudice'}
print("-------------------------------")
#setler true ve false mantıksal operatörler ile karşılaştırılabilir.
print(set_a > set_b)  # Output: False
print(set_a < set_b)  # Output: True