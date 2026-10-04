#dictionary 
#temel özellikleri
#1. Değiştirilebilir (mutable) veri tipidir.
#2. Sırasızdır (unordered).
#3. Anahtar-değer (key-value) çiftlerinden oluşur.
#4. Anahtarlar benzersizdir (unique).
#dictionary ile ilgili örnekler:
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student)
#dict() hazır metodu ile dictionary oluşturma
student2 = dict(name="Bob", age=22, grade="B")
print(student2)
#elemanlara erişim yöntemleri
print(student["name"])  # Output: Alice
#get() metodu ile erişim
#get metodu, belirtilen anahtara karşılık gelen değeri döndürür. Eğer anahtar bulunamazsa, None döndürür veya belirtilen varsayılan değeri döndürebilir.
print(student.get("age"))  # Output: 20
print(student.get("height", "Height not found"))  # Output: Height not found
print("-------------------------------")
#esnek veri türleri ve eleman sayısı
print(f"Student: {student}")
print(f"Number of elements in student: {len(student)}")
#sözlük metodlaı ve dinamik canlı görünümler 
#.keys() metodu: sözlüğün anahtarlarını döndürür.
print(student.keys())  # Output: dict_keys(['name', 'age', 'grade'])
#.values() metodu: sözlüğün değerlerini döndürür.
print(student.values())  # Output: dict_values(['Alice', 20, 'A'])
#.items() metodu: sözlüğün anahtar-değer çiftlerini döndürür.
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])
#in anahtar kelimesi ile anahtar var mı yok mu kontrolü
print("name" in student)  # Output: True
#veri güncelleme ve ekleme işlemleri
student["age"] = 21  # Update the age
student["major"] = "Computer Science"  # Add a new key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 21,
#update() metodu: bir sözlüğü başka bir sözlükle günceller.
student.update({"age": 22, "grade": "B"})
print(student)  # Output: {'name': 'Alice', 'age': 22, 'grade': 'B', 'major': 'Computer Science'}
#veri ve sözlük silme yöntemleri
#del anahtar kelimesi ile silme
del student["major"]  # Remove the key-value pair with key "major"
#pop() metodu: belirtilen anahtara karşılık gelen anahtar-değer çiftini siler ve değeri döndürür.
removed_grade = student.pop("grade")
print(f"Removed grade: {removed_grade}")  # Output: Removed grade: B
#popitem() metodu: sözlüğün son eklenen anahtar-değer çiftini siler ve bir tuple olarak döndürür.
removed_item = student.popitem()
print(f"Removed item: {removed_item}")  # Output: Removed item: ('age', 22)
#clear() metodu: sözlüğün tüm elemanlarını siler.
student.clear()
print(student)  # Output: {}
print("-------------------------------")
#dictionary yapısında döngüler 
for key in student:
    print(f"Key: {key}, Value: {student[key]}")
#new example
cars = {"brand": "Toyota",
    "model": "Corolla",
    "year": 2020}
for key, value in cars.items():
    print(f"Key: {key}, Value: {value}")
#dictionary kopyalama mantığı
#1. copy() metodu: bir sözlüğün kopyasını oluşturur.
student_copy = student.copy()
print(f"Student copy: {student_copy}")
#dictionary comprehension ile sözlük oluşturma
squared_numbers = {x: x**2 for x in range(5)}
print(f"Squared numbers: {squared_numbers}")
#dict() kurucu ile sözlük oluşturma
new_dict = dict(name="Alice", age=20, grade="A")    
print(f"New dictionary: {new_dict}")
#iç içe sözlükler (nested dictionaries) ile ilgili örnek
nested_dict = {
    "student1": {"name": "Alice", "age": 20, "grade": "A"},
    "student2": {"name": "Bob", "age": 22, "grade": "B"}
}
print(f"Nested dictionary: {nested_dict}")
#iç içe döngüler ile iç içe sözlük elemanlarına erişim
for student_key, student_info in nested_dict.items():
    print(f"Student Key: {student_key}")
    for info_key, info_value in student_info.items():
        print(f"  {info_key}: {info_value}")

#ileri düzey sözcük işlemleri ve örnekler
#fromkeys() metodu: belirtilen anahtarlar için bir sözlük oluşturur.
keys = ["name", "age", "grade"]
default_value = "Unknown"
new_student = dict.fromkeys(keys, default_value)
print(f"New student with default values: {new_student}")
#setdefault() metodu: belirtilen anahtar için bir değer döndürür; eğer anahtar yoksa, belirtilen varsayılan değeri ekler.
student.setdefault("major", "Undeclared")
print(f"Student after setdefault: {student}")
