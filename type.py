#txt type = str
#örnek: "Hello, World!"
#numeric type = int,float,complex
#örnek: 1, 1.5, 1+2j
#sequence type = list,tuple,range
#örnek: [1, 2, 3], (1, 2, 3), range(1, 4)
#mapping type = dict
#örnek: {"name": "John", "age": 30}
#set type = set,frozenset
#örnek: {1, 2, 3}, frozenset({1, 2, 3})


print("----------------------------------------------------------------" \
"")
mylist = [1, 2, 3]
print(mylist)
mylist1 =["black", "white", "red"]

print(mylist1)
print("----------------------------------------------------------------" \
"")
#mapping type = dict
mydict = {"name": "John", "age": 30}
print(mydict)
print("----------------------------------------------------------------" \
"")
#set type = set,frozenset
myset = {1, 2, 3}
print(myset)
print("----------------------------------------------------------------" \
"")
mybool = True
print(type(mybool))
print("----------------------------------------------------------------" \
"")
import sys 
x = 5
print(sys.getsizeof(x))
#kaç byte yer kapladığını gösterir c den farklı olarak python da değişkenin tipine göre yer kaplar.
print("----------------------------------------------------------------" \
"")
name = b"John"
print(type(name))
print(bytes(name))
print("----------------------------------------------------------------" \
"")
#memoryview type = memoryview şu işe yarar: bir byte dizisinin bellekteki görünümünü sağlar. Bu, büyük veri kümeleriyle çalışırken bellek kullanımını optimize etmek için kullanılabilir.
                 