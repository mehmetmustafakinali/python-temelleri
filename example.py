#for döngüsü ile obeb okek bulma
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
smaller = min(number1, number2)
#min burada iki sayıdan küçük olanı bulmak için kullanılır
for i in range(smaller, 0, -1):
    if number1 % i == 0 and number2 % i == 0:
        gcd = i
        break
lcm= (number1 * number2) // gcd
#obeb okek hesaplama
print(f"GCD of {number1} and {number2} is: {gcd}")#obeb
print(f"LCM of {number1} and {number2} is: {lcm}")#okek

print("------------------------------")

#fibonacci serisi for döngüsü ile hesaplama
n = int(input("Enter the number of terms for Fibonacci series: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_series = []
    first, second = 0, 1
    for _ in range(n):
        fibonacci_series.append(first)
        temp = first + second
        first = second
        second = temp
    print(f"Fibonacci series up to {n} terms: {fibonacci_series}")
            