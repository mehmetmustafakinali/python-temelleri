#fonksiyonlar 
#özellikler:
# - Parametre alabilir
# - Geriye değer döndürebilir
# - Kendi içinde çalışabilen kod bloklarıdır
#hazır fonksiyonlar: print(), len(), type(), range(), input() gibi
#kodları kümelemek ve tekrar kullanılabilir hale getirmek için fonksiyonlar kullanılır.
#örnek : toplama , çıkarma, çarpma, bölme gibi işlemler için fonksiyonlar yazılabilir.
#argüman : fonksiyon çağrılırken fonksiyona gönderilen değerlerdir.örn: add(5, 3) fonksiyon çağrısında 5 ve 3 argümanlardır.
#paramtre : fonksiyon tanımlanırken fonksiyona gönderilen değerleri temsil eden değişkenlerdir.örn: def add(a, b): fonksiyon tanımında a ve b parametrelerdir.

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
add(5, 3)
subtract(5, 3)
multiply(5, 3)
divide(5, 0)
divide(5, 2)
#dinamik / belirsiz sayıda argüman alan fonksiyonlar *args ve **kwargs ile yapılabilir.
def dynamic_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

dynamic_function(1, 2, 3, name="Alice", age=25)
def books(*books):
    for book in books:
        print(book)
books("Book 1", "Book 2", "Book 3")
# * ile normal arasındaki fark *args, **kwargs ile belirsiz sayıda argüman alabilen fonksiyonlar yazılır.
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"
full_name("John", "Doe")
#ANAHTAR KELİME ARÜMANLARI (KEYWORD ARGUMENTS) : fonksiyon çağrılırken parametrelerin isimleri belirtilerek argümanlar gönderilebilir.örn: full_name(first_name="John", last_name="Doe")
def my_function(name1 , name2 , name3 ):
    print(f"Name 1: {name1}")
    print(f"Name 2: {name2}")
    print(f"Name 3: {name3}")
#anahtarlar anahatar = değer şeklinde gönderilir.örn: my_function(name1="Alice", name2="Bob", name3="Charlie")
my_function(name1="Alice", name2="Bob", name3="Charlie")
#dinamik sayıda anahtar kelime argümanı alan fonksiyonlar **kwargs ile yapılabilir.örn: def my_function(**kwargs): print(kwargs)
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
person_info(name="Alice", age=30, city="New York")
#varsayılan paramatre değerleri default parameter values ile yapılabilir.örn: def greet(name="Guest"): print(f"Hello, {name}!")
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
#burada bu şekilde yapmak aşırı yükleme (overloading) mantığı ile yapılabilir.örn: def greet(name=None): if name is None: print("Hello, Guest!") else: print(f"Hello, {name}!")
def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!
#karmaşık veri tiplerinde argüman gönderme ve alma işlemleri yapılabilir.örn: def process_data(data): print(data)
def my_fruit_func(food):
    for item in food:
        print(item)
fruits = ["apple", "banana", "cherry"]
my_fruit_func(fruits)
print("-------------------------------" )
#return ifadesi ve print ifadesi arasasındaki fark: return ifadesi fonksiyondan bir değer döndürür ve fonksiyonun çalışmasını sonlandırır. print ifadesi ise ekrana çıktı verir ancak fonksiyonun çalışmasını sonlandırmaz.
def my_sum(a,b):
    return a + b 
result = my_sum(5, 3)
print(result)  # Output: 8
new_result = my_sum(10, 20)
print(new_result*5)  # Output: 150
print("-------------------------------")
#iç içe fonksiyon çağrıları (nested function calls) ile ilgili örnek
def my_sume(a, b):
    return a + b
print(my_sume(my_sume(2, 3), my_sume(4, 5)))  # Output: 14
#boş fonksiyon tanımlama 
def empty_function():
    pass
#PASS YEERİNE ... 
def another_empty_function():
    ...  # This is a placeholder for future code
#sadece konumsal argüman zorunluluğu 
def my_fun(x, y, /):
    return x + y
my_fun(2, 3)  # Valid
#my_fun(x=2, y=3)  # Invalid, will raise a TypeError
#sadece anahtar kelime argüman zorunluluğu
def my_fun2(*, x, y):
    return x + y
my_fun2(x=2, y=3)  # Valid
#my_fun2(2, 3)  # Invalid, will raise a TypeError
#konumsal ve anahtar kelime argümanlarını birleştirme
def my_fun3(x, y, /, *, z):
    return x + y + z
my_fun3(2, 3, z=4)  # Valid
#döngüler içinde fonksiyon kullanımı 
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(5)  # Output: 0 1 2 3 4
print("-------------------------------")
#birden fazla return ifadesi kullanımı ve tuple ile return etme
def check_numbers(a, b):
    if a > b:
        return (a, "is greater than", b)
    elif a < b:
        return (a, "is less than", b)
    else:
        return (a, "is equal to", b)
check_result = check_numbers(5, 3)
print(check_result)
print(check_result[0], check_result[1], check_result[2])  # Output: 5 is greater than 3
print("-------------------------------")
#fonsiyon içinde başka bir fonksiyon kullanma 
def sum_numbers(a,b):
    return a + b
def square_number(n):
    return n * n
def sum_and_square(a, b):
    sum_result = sum_numbers(a, b)
    square_result = square_number(sum_result)
    return square_result
result = sum_and_square(2, 3)
print(result)  # Output: 25
print("-------------------------------")
#iç içe fonksiyonlar (nested functions) ile ilgili örnek
def outer_function(name):
    def greeting():
        return f"Hello, {name}!"
    return greeting()
print(outer_function("Alice"))  # Output: Hello, Alice!
print("-------------------------------")
#return ile birden fazla değer döndürme ve tuple ile return etme
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result
result = calculate(10, 5)
print(result)  # Output: (15, 5)
print(f"Sum: {result[0]}, Difference: {result[1]}")  # Output: Sum: 15, Difference: 5
print("-------------------------------")
#fonksiyonu başka bir fonksiyona paramaetre olarak gönderme ve fonksiyon içinde çağırma
def multiply(a=1, b=1):
    return a * b
def apply_function(func, x, y):
    return func(x, y)
result = apply_function(multiply, 5, 3)
print(result)  # Output: 15
print("-------------------------------")
#kapsam scope ile ilgili örnek
#global veriable: fonksiyon dışında tanımlanan değişkenlerdir ve tüm fonksiyonlar tarafından erişilebilir.
#local veriable: fonksiyon içinde tanımlanan değişkenlerdir ve sadece o fonksiyon içinde erişilebilir.
#isim çakışması: global ve local değişkenlerin aynı isimde olması durumunda local değişken önceliklidir.
x = "global"
def my_function():
    x = "local"
    print("Inside function:", x)  # Output: Inside function: local
my_function()
print("python is " +  x )  # Output: python is global
print("-------------------------------")
#global anahtar sözcük kullanımı 
x = "global"
def my_function2():
    global x #burada global anahtar kelimesi ile fonksiyon içinde global değişkeni kullanabiliriz.
    x = "local"
    print("Inside function:", x)  # Output: Inside function: local
my_function2()
print("Outside function:", x)  # Output: Outside function: local
print("-------------------------------")
#özyinelemeli fonksiyonlar (recursive functions) ile ilgili örnek
#faktoriyel hesabı 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
print("-------------------------------")
#fibonacci dizisi hesabı
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print("-------------------------------")
# 1 den n kadar olan sayıların toplamı
def some_recursion(n):
    if n > 0 :
        return n + some_recursion(n - 1)
    else: 
        return 0 
print(some_recursion(9))  # Output: 15
print("-------------------------------")
#return fonksiyonu ile sonlandırma etkisi 
def check_status():
    return 0 
    print("hello")
check_status()


