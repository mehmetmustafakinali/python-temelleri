#Bitsel atama operatorleri
a = 10
a &= 5  # a = a & 5
print("After bitwise AND, a =", a)
a |= 3  # a = a | 3
print("After bitwise OR, a =", a)
a ^= 2  # a = a ^ 2
print("After bitwise XOR, a =", a)
#ve operatörü 
b = 7
c = 3
d = b and c
print("After logical AND, d =", d)
#veya operatörü 
g = 7
h = 3
i = g or h
print("After logical OR, i =", i)
#not operatörü
j = True
k = not j
print("After logical NOT, k =", k)
#özel veya operatörü
l = 7
m = 3
n = l ^ m
print("After bitwise XOR, n =", n)
#özel ve operatörü
o = 7
p = 3
q = o & p
print("After bitwise AND, q =", q)
#şimdi bu örnekler ile ilgili bir program yazalım
a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
c = a + b
print("After addition, c =", c)
d = a - b
print("After subtraction, d =", d)
e = a * b
print("After multiplication, e =", e)
f = a / b
print("After division, f =", f)
g = a % b
print("After modulo, g =", g)
h = a ** b
print("After exponentiation, h =", h)
i = a // b
print("After integer division, i =", i)
#bitsel opeatörler ile ilgili kapsamlı bir örnek
j = int(input("Enter a number for j: "))
k = int(input("Enter a number for k: "))
l = j & k
print("After bitwise AND, l =", l)
m = j | k
print("After bitwise OR, m =", m)
n = j ^ k
print("After bitwise XOR, n =", n)
o = ~j
print("After bitwise NOT, o =", o)
#right shift ve left shift operatörleri ile ilgili bir örnek
p = int(input("Enter a number for p: "))
q = p << 2
print("After left shift, q =", q)
r = p >> 2
print("After right shift, r =", r)
#right shift ve left shift operatörleri ile ilgili bir örnek
s = int(input("Enter a number for s: "))
t = s << 3
print("After left shift, t =", t)
u = s >> 3
print("After right shift, u =", u)
#right shift ve left shift şu işe yarar: bir sayının binary gösteriminde bitleri sağa veya sola kaydırır. Bu işlem sayıyı 2'nin kuvvetleriyle çarpmak veya bölmek gibi düşünülebilir. Örneğin, bir sayıyı 1 bit sola kaydırmak, sayıyı 2 ile çarpmak anlamına gelirken, 1 bit sağa kaydırmak, sayıyı 2 ile bölmek anlamına gelir.
#bitsel operatörlerin gerçek hayatta kullanım alanları 
#şifreleme 
#veri sıkıştırma 
#soketler üzerinden ağ iletişimi 
#gömülü sistemler programlama
#donanım ve devre tasarım 
#walrus operatörü (:=) ile ilgili bir örnek
x = 5
if (n := x * 2) > 10:
    print(f"Double of {x} is {n}, which is greater than 10.")
#burada walrus operatörü (:=) kullanılarak x'in iki katı olan n değişkeni atanıyor ve aynı zamanda if koşulunda kontrol ediliyor. Eğer n 10'dan büyükse, ekrana bir mesaj yazdırılıyor. Bu operatör, bir değeri atarken aynı zamanda bir koşulda kullanmamıza olanak tanır ve kodu daha temiz ve okunabilir hale getirir.
x=10
print(x:=5)  # x'i 5 ile karşılaştırır ve x'in değerini günceller, ardından True veya False döndürür.



