if 70>7:
    print("70 is greater than 7")
else:
    print("70 is not greater than 7")
#koşullarla ilgili örnekler 
if 5>10:
    print("5 is greater than 10")
elif 5<10:
    print("5 is less than 10")
elif 5==10:
    print("5 is equal to 10")
else:
    print("5 is not equal to 10")
#girilen sayının pozitif, negatif veya sıfır olduğunu kontrol eden bir program
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#pythonda bool veri türü
is_true = True
is_false = False
print(is_true)
print(is_false)
#koşul ifadeleri ile bool veri türü
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
    is_adult = False
    print(is_adult)
    print(type(is_adult))
    print(is_adult == False)
    print(not is_adult)
    print(is_adult is False)
    print(is_adult is not True)
#bu örnek kullanıcının girdiği sayının tek mi çift mi olduğunu kontrol eder
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    is_even = False
    print(is_even)
 
