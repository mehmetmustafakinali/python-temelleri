#string formatlama
# .format() metodu
#örnek 1
age = 25
txt = "My name is John, and I am {}"
print(txt.format(age))
#veya 
age = 25
txt = "My name is John, and I am {0}".format(age)
print(txt)
#format metodu şu işe yarar : bir string içindeki {} işaretlerini, format metoduyla verilen değerlerle doldurur.
#çoklu değerler de verilebilir
name = "John"
age = 36
txt = "My name is {0}, and I am {1}".format(name, age)
print(txt)
#birde f stringler var. f-stringler, Python 3.6 ile birlikte gelen bir özelliktir ve string formatlamayı daha kolay ve okunabilir hale getirir.
#örnek 1
name = "John"
age = 36
txt = f"My name is {name}, and I am {age}"
print(txt)
#float sayıları formatlamak için de f-stringler kullanılabilir. Örneğin, bir float sayıyı belirli bir ondalık basamak sayısına yuvarlamak için f-stringler kullanılabilir.
#örnek 2
price = 49.99
txt = f"The price is {price:.2f}"
print(txt)
#buradaki .2f ifadesi, price değişkeninin değerini 2 ondalık basamakla formatlar. Yani, 49.99 sayısı 49.99 olarak yazdırılır.
#onun yerine, 49.9 gibi bir sayı yazdırmak isterseniz, .1f ifadesini kullanabilirsiniz. Örneğin:
price = 49.99
txt = f"The price is {price:.1f}"
print(txt)
#örnek 3 
midterm_exem_score=input("Enter your midterm exam score: ")
final_exam_score=input("Enter your final exam score: ")
average_score=(float(midterm_exem_score)+float(final_exam_score))/2
print(f"Your average score is: {average_score:.2f}") 

print("---------------------------------------------")

#string metotları
#capitalize() metodu, bir stringin ilk harfini büyük yapar ve diğer tüm harfleri küçük yapar. Örneğin, "hello world" stringi capitalize() metodu ile "Hello world" olarak değiştirilir.       
#örnek 1
txt = "hello world"
print(txt.capitalize())
#casefold() metodu, bir stringin tüm harflerini küçük yapar ve Unicode karakterlerini de dikkate alır. Örneğin, "HELLO WORLD" stringi casefold() metodu ile "hello world" olarak değiştirilir.
#örnek 2
txt = "HELLO WORLD"
print(txt.casefold())
#lowerden farkı casefold() metodu, Unicode karakterlerini de dikkate alarak tüm harfleri küçük yapar. lower() metodu ise sadece ASCII karakterlerini küçük yapar.
#title() metodu, bir stringin her kelimesinin ilk harfini büyük yapar ve diğer tüm harfleri küçük yapar. Örneğin, "hello world" stringi title() metodu ile "Hello World" olarak değiştirilir.
txt = "hello world"
print(txt.title())
#swapcase işlemi büyük olanı küçültür ve küçük olanı büyütür. Örneğin, "Hello World" stringi swapcase() metodu ile "hELLO wORLD" olarak değiştirilir.
txt = "Hello World"
print(txt.swapcase())
#islower() metodu, bir stringin tüm harflerinin küçük olup olmadığını kontrol eder. Eğer tüm harfler küçükse True, aksi takdirde False döner. Örneğin, "hello world" stringi islower() metodu ile True dönerken, "Hello World" stringi False döner.
txt = "hello world"
print(txt.islower())
#isupper() metodu, bir stringin tüm harflerinin büyük olup olmadığını kontrol eder. Eğer tüm harfler büyükse True, aksi takdirde False döner. Örneğin, "HELLO WORLD" stringi isupper() metodu ile True dönerken, "Hello World" stringi False döner.
txt = "HELLO WORLD"
print(txt.isupper())   
#center ise bir stringi belirli bir genişlikte ortalar ve boşluklarla doldurur. Örneğin, "hello" stringi center() metodu ile 10 karakter genişliğinde ortalanır ve boşluklarla doldurulur.
txt = "hello"   
result = txt.center(10)
print(result) 
#isdigit() metodu, bir stringin sadece rakamlardan oluşup oluşmadığını kontrol eder. Eğer string sadece rakamlardan oluşuyorsa True, aksi takdirde False döner. Örneğin, "12345" stringi isdigit() metodu ile True dönerken, "123a45" stringi False döner.
txt = "12345"
print(txt.isdigit())
#isidentifier() metodu, bir stringin geçerli bir Python tanımlayıcısı olup olmadığını kontrol eder. Eğer string geçerli bir tanımlayıcı ise True, aksi takdirde False döner. Örneğin, "my_variable" stringi isidentifier() metodu ile True dönerken, "my-variable" stringi False döner.
txt = "my_variable"
print(txt.isidentifier())
txt = "my-variable"
print(txt.isidentifier())
#islower metodu, bir stringin tüm harflerinin küçük olup olmadığını kontrol eder. Eğer tüm harfler küçükse True, aksi takdirde False döner. Örneğin, "hello world" stringi islower() metodu ile True dönerken, "Hello World" stringi False döner.
txt = "hello world"
print(txt.islower())
#isupper metodu, bir stringin tüm harflerinin büyük olup olmadığını kontrol eder. Eğer tüm harfler büyükse True, aksi takdirde False döner. Örneğin, "HELLO WORLD" stringi isupper() metodu ile True dönerken, "Hello World" stringi False döner.
txt = "HELLO WORLD"
print(txt.isupper())
#isnumeric() metodu, bir stringin sadece sayılardan oluşup oluşmadığını kontrol eder. Eğer string sadece sayılardan oluşuyorsa True, aksi takdirde False döner. Örneğin, "12345" stringi isnumeric() metodu ile True dönerken, "123a45" stringi False döner.
txt = "12345"
print(txt.isnumeric())
tyxt = "123a45"
print(tyxt.isnumeric())
#isprintable() metodu, bir stringin yazdırılabilir olup olmadığını kontrol eder. Eğer string yazdırılabilir karakterlerden oluşuyorsa True, aksi takdirde False döner. Örneğin, "hello world" stringi isprintable() metodu ile True dönerken, "\n" stringi False döner.
txt = "hello world"
print(txt.isprintable())
txt = "\n"
print(txt.isprintable())
#isspace() metodu, bir stringin sadece boşluk karakterlerinden oluşup oluşmadığını kontrol eder. Eğer string sadece boşluk karakterlerinden oluşuyorsa True, aksi takdirde False döner. Örneğin, "   " stringi isspace() metodu ile True dönerken, "hello world" stringi False döner.
txt = "   "
print(txt.isspace())
txt = "hello world"
print(txt.isspace())
#istitle() metodu, bir stringin baş harflerinin büyük olup olmadığını kontrol eder. Eğer stringin baş harfleri büyükse True, aksi takdirde False döner. Örneğin, "Hello World" stringi istitle() metodu ile True dönerken, "hello world" stringi False döner.
txt = "Hello World"
print(txt.istitle())
#join() metodu, bir stringin elemanlarını birleştirerek yeni bir string oluşturur. Örneğin, ["Hello", "World"] listesi join() metodu ile "Hello World" olarak birleştirilir.
mylist = ["Hello", "World"]
x = " ".join(mylist)
print(x)
#separator olarak kullanılacak stringi join() metoduna vererek, listede bulunan elemanları birleştirebiliriz. Örneğin, ["Hello", "World"] listesi join() metodu ile "-" separatoru kullanılarak "Hello-World" olarak birleştirilir.
mylist = ["Hello", "World"]
x = "-".join(mylist)
print(x)
#dictionary ile join() metodu kullanmak için, dictionaryin keys() veya values() metodunu kullanabiliriz. Örneğin, {"name": "John", "age": 36} dictionaryi join() metodu ile "-" separatoru kullanılarak "name-age" olarak birleştirilir.
mydict = {"name": "John", "age": 36}
x = "-".join(mydict.keys())
print(x)
#ljust() metodu, bir stringin sol tarafını belirli bir genişlikte doldurur ve sağ tarafını boşluklarla doldurur. Örneğin, "hello" stringi ljust() metodu ile 10 karakter genişliğinde sola yaslanır ve sağ tarafı boşluklarla doldurulur.
txt = "hello"
print(txt.ljust(10))
#rjust() metodu, bir stringin sağ tarafını belirli bir genişlikte doldurur ve sol tarafını boşluklarla doldurur. Örneğin, "hello" stringi rjust() metodu ile 10 karakter genişliğinde sağa yaslanır ve sol tarafı boşluklarla doldurulur.
txt = "hello"
print(txt.rjust(10))
#strip metodu, bir stringin başındaki ve sonundaki boşlukları kaldırır. Örneğin, "   hello   " stringi strip() metodu ile "hello" olarak değiştirilir.
txt = "   hello   "
print(txt.strip())
#maketrans() metodu, bir stringin karakterlerini başka karakterlerle değiştirmek için kullanılır. Örneğin, "hello" stringi make_trans() metodu ile "jgnnq" olarak değiştirilir.
txt = "hello"
trans = txt.maketrans("h", "j")
print(txt.translate(trans))
#partition() metodu, bir stringi belirli bir ayırıcıya göre üç parçaya böler. Örneğin, "hello world" stringi partition() metodu ile "hello", " ", "world" olarak üç parçaya ayrılır.
txt = "hello world"
print(txt.partition(" "))
#replace() metodu, bir stringin belirli bir karakterini başka bir karakterle değiştirir. Örneğin, "hello world" stringi replace() metodu ile "hello python" olarak değiştirilir.
txt = "hello world"
print(txt.replace("world", "python"))
#rpartition() metodu, bir stringi belirli bir ayırıcıya göre üç parçaya böler. Örneğin, "hello world" stringi rpartition() metodu ile "hello", " ", "world" olarak üç parçaya ayrılır.
txt = "hello world"
print(txt.rpartition(" "))
#rfind() metodu, bir stringin belirli bir karakterini arar ve bulduğu ilk indeksi döndürür. Örneğin, "hello world" stringi rfind() metodu ile "o" karakterinin bulunduğu son indeksi döndürür.
txt = "hello world"
print(txt.rfind("o"))
#rindex() metodu, bir stringin belirli bir karakterini arar ve bulduğu ilk indeksi döndürür. Örneğin, "hello world" stringi rindex() metodu ile "o" karakterinin bulunduğu son indeksi döndürür.
txt = "hello world"
print(txt.rindex("o"))
#split() metodu, bir stringi belirli bir ayırıcıya göre böler ve bir liste döndürür. Örneğin, "hello world" stringi split() metodu ile ["hello", "world"] olarak iki parçaya ayrılır.
txt = "hello world"
print(txt.split(" "))
#rsplit() metodu, bir stringi belirli bir ayırıcıya göre böler ve bir liste döndürür. Örneğin, "hello world" stringi rsplit() metodu ile ["hello", "world"] olarak iki parçaya ayrılır.
txt = "hello world"
print(txt.rsplit(" "))
#splitlines() metodu, bir stringi satır sonlarına göre böler ve bir liste döndürür. Örneğin, "hello\nworld" stringi splitlines() metodu ile ["hello", "world"] olarak iki parçaya ayrılır.
txt = "hello\nworld"
print(txt.splitlines())
#zfill() metodu, bir stringin başına belirli bir sayıda sıfır ekler. Örneğin, "hello" stringi zfill() metodu ile "000hello" olarak değiştirilir.
txt = "hello"
print(txt.zfill(10))
