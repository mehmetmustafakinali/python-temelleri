#karşılaştırma operatörleri ile ilgili bir örnek
a = 5
b = 10
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
#eşittir operatörü ile ilgili bir örnek
c = 5
d = 5
if c == d:
    print("c is equal to d")
    print("The values are the same.")
#eşit değildir operatörü ile ilgili bir örnek
e = 5
f = 10
if e != f:
    print("e is not equal to f")
    print("The values are different.")
#büyük eşit operatörü ile ilgili bir örnek
g = 5
h = 5
if g >= h:
    print("g is greater than or equal to h")
    print("The values are the same or g is greater.")
#küçük eşit operatörü ile ilgili bir örnek
i = 5
j = 10
if i <= j:
    print("i is less than or equal to j")
    print("The values are the same or i is less.")
#kapsamlı örnek şifre doğrulama programı
real_password = "python123"
my_password = input("Enter your password: ")
if my_password == real_password:
    print("Password is correct.")
else:
    print("Password is incorrect.")
#girilen sayının tek mi çift mi olduunu bulan algoritma 
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
elif number % 2 != 0:
    print("The number is odd.")
else:
    print("The number is neither even nor odd.")


print("----------------------------------------------")

#python mantıksal ve kimlik operatörler 
#ve operatörü ile ilgili bir örnek
score = int(input("Enter your score: "))
if score >= 50 and score <= 100:
    print("You passed the exam.")
    print("Congratulations!")
else:
    print("You failed the exam.")
    print("Better luck next time.")
#veya operatörü ile ilgili bir örnek
age = int(input("Enter your age: "))
if age < 18 or age > 65:
    print("You are not eligible for this program.")
    print("Please try again later.")
else:
    print("You are eligible for this program.")
    print("Welcome!")
#not operatörü ile ilgili bir örnek
is_raining = input("Is it raining? (yes/no): ")
if not is_raining.lower() == "yes":
    print("You can go outside.")
    print("Enjoy the weather!")
else:
    print("You should stay inside.")
    print("Better to be safe than sorry.")
#kimlik operatörleri ile ilgili bir örnek
x = [1, 2, 3]
y = [1, 2, 3]
if x is y:
    print("x and y are the same object.")
else:
    print("x and y are different objects.")
    print("Even though they have the same values, they are not the same object in memory.")
#is operatörü ile ilgili bir örnek
z = [1, 2, 3]
w = z
if z is w:
    print("z and w are the same object.")
else:
    print("z and w are different objects.")

