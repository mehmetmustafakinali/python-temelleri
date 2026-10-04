#listlerle donguler kullanımı 
fruits = ["apple", "banana", "cherry", "banana", "kiwi", "mango"]

for fruit in fruits:
    print(fruit)
#index numarları ile ulaşma
print("------------------------------")
 
for item in range(len(fruits)):
    print(fruits[item])
#bu şekilde de index numaraları ile ulaşabiliriz
print("------------------------------")
#while döngüsü ile birlikte break komutu kullanımı
i = 0 
while i < len(fruits):
    print(fruits[i])
    i += 1
#list comprehension ile birlikte for döngüsü kullanımı
#list comprehension ne demek :  Bir listeyi oluşturmak için kullanılan bir yol.
print("------------------------------")
print([fruit for fruit in fruits])
#veyaa 
print("------------------------------")
[print(item) for item in fruits]
print("------------------------------")
new_list=[]
for item in fruits:
    if "a" in item:
        new_list.append(item)
        print(item)
print("------------------------------")
#list comprehension ile birlikte for döngüsü ve if kullanımı
new_list2 = [item for item in fruits if "a" in item]
print(new_list2)


