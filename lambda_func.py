#lamda fonksiyonları: lambda fonksiyonları, tek satırlık anonim fonksiyonlardır.
#normalde 
import math
def fonksiyon_adi(a, b):
    return a + b
#lambda ile
lambda_fonksiyon = lambda a, b: a + b
#birden fazla parametere kullanma 
some_sum = lambda x, y, z: x + y + z
print(some_sum(1, 2, 3))  # Output: 6
print(math.sqrt(16))  # Output: 4.0
#2 parametreli çarpma örneği 
mutiply = lambda x, y: x * y
print(mutiply(3, 4))  # Output: 12
#koşullu ifadeler ile lambda fonksiyonları
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(5))  # Output: Odd
print(check_even(6))  # Output: Even
# list ve map fonk ile birlikte kullanımı
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
#birden fazla parametreli lambda fonksiyonları
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
list_of_sums = list(map(lambda x: x[0] + x[1], list_of_tuples))
print(list_of_sums)  # Output: [3, 7, 11]
print("-------------------------------")
#numbers listesi içindeki çift sayıları filtreleme
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)  # Output: [2, 4]
#map() içerisinde koşullu ifadeler kullanma
result = list(map(lambda x: x * 2 if x % 2 == 0 else x, numbers))
print(result)  # Output: [1, 4, 3, 8, 5]
#fiter() ile birlikte lambda fonksiyonları kullanma
result = list(filter(lambda x: x > 3, numbers))
print(result)  # Output: [4, 5]
print("-------------------------------")
#metnin uzunluğununa göre filtreleme len() kullanımı 
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
long_fruits = list(filter(lambda fruit: len(fruit) > 5, fruits))
print(long_fruits)  # Output: ['banana', 'cherry', 'elderberry']
print("-------------------------------")
#metnin uzunluğuna göre sıralama
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_fruits = sorted(fruits, key=lambda x: len(x))
print(sorted_fruits)  # Output: ['date', 'apple', 'banana', 'cherry', 'elderberry']
print("-------------------------------")
#sorted fonksiyonu ile birlikte lambda fonksiyonları kullanma
#sorted() fonksiyonu elemanları sıralamak için kullanılır 
#örnek:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
print("-------------------------------")
#lamda ile abs() fonksiyonu kullanımı
numbers = [-5, -2, 0, 3, 7]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print(sorted_by_abs)  # Output: [0, -2, 3, -5, 7]
print("-------------------------------")
#fonksiyon içinde lambda fonksiyonu kullanımı
def my_function(n):
    return lambda x: x * n
double = my_function(2)
print(double(5))  # Output: 10
multiply_by_3 = my_function(3)
print(multiply_by_3(5))  # Output: 15
