#mach fonksiyonları 
#min() ve max() fonksiyonları
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")

#abs() fonksiyonu : mutlak değer hesaplar 
print(f"Absolute value of -5: {abs(-5)}")

#round() fonksiyonu : sayısal değeri yuvarlar
print(f"Rounded value of 3.14159: {round(3.14159, 2)}")

#pow() fonksiyonu : üs alma işlemi yapar
print(f"2 to the power of 3: {pow(2, 3)}")

#sum() fonksiyonu : bir iterable içindeki sayıları toplar
print(f"Sum of numbers: {sum(numbers)}")
#math modülleri ve matematiksel sabitler ile ilgili örnekler
#math.e : euler sayısı (yaklaşık 2.718)
#math.pi : pi sayısı (yaklaşık 3.14159)
#math.tau : tau sayısı (yaklaşık 6.28318)
#math.inf : sonsuzluk 
#math.nan : sayısal olmayan değer (Not a Number)
import math
print(f"Euler's number: {math.e}")
print(f"Pi: {math.pi}")
print(f"Tau: {math.tau}")
print(f"Infinity: {math.inf}")
print(f"Not a Number: {math.nan}")
#trigonometric functions (trigonometrik fonksiyonlar) ile ilgili örnekler
print(f"Sin of 0: {math.sin(0)}")
print(f"Cos of 0: {math.cos(0)}")
print(f"Tan of 0: {math.tan(0)}")
print(f"Arcsin of 0: {math.asin(0)}")
print(f"Arccos of 1: {math.acos(1)}")
print(f"Arctan of 0: {math.atan(0)}")
#açılış dönüşüm metodları 
print(f"Degrees to radians: {math.radians(180)}") # radians : ne kadar radyan olduğunu verir
print("-------------------------------")
print(f"Radians to degrees: {math.degrees(math.pi)}") # degrees : ne kadar derece olduğunu verir
#math.ceil() : sayıyı yukarı yuvarlar
print("-------------------------------")
print(f"Ceiling of 3.2: {math.ceil(3.2)}")
#math.floor() : sayıyı aşağı yuvarlar
print("-------------------------------")
print(f"Floor of 3.8: {math.floor(3.8)}")
#math.sqrt() : sayının karekökünü alır
print("-------------------------------")
print(f"Square root of 16: {math.sqrt(16)}")
#math.isqrt() : sayının pozitif tam kare olup olmadığını kontrol eder
print(f"Is 16 a perfect square? {math.isqrt(16) ** 2 == 16}")
#math.trunc() : sayının tam kısmını alır
print("-------------------------------")
print(f"Truncated value of 3.9: {math.trunc(3.9)}")
#math.remainder() : sayının bölümünden kalanı alır
print(f"Remainder of 10 divided by 3: {math.remainder(10, 3)}")
print("-------------------------------")
print(f"Remainder of 10 divided by 3 using % operator: {10 % 3}")
print("-------------------------------")
print(f"Remainder of 10 divided by 3 using divmod(): {divmod(10, 3)[1]}")
print("-------------------------------")
#math.comb() : kombinasyon hesaplar
print(f"Combination of 5 choose 2: {math.comb(5, 2)}")
print("-------------------------------")
#math.copysign(x,y) : x'in işaretini y'nin işareti ile değiştirir
print(f"Copy sign of -3.5 to 2.0: {math.copysign(-3.5, 2.0)}")
print("-------------------------------")
#math.dist() : iki nokta arasındaki öklidyen mesafeyi hesaplar
point1 = (1, 2)
point2 = (4, 6)
print(f"Distance between {point1} and {point2}: {math.dist(point1, point2)}")
print("-------------------------------")
#MATH.ERFc() : hata fonksiyonu (error function) hesaplar
print(f"Error function of 1: {math.erfc(1)}")
print("-------------------------------")
#math.exp() : e üzeri x hesaplar
print(f"e to the power of 2: {math.exp(2)}")
print("-------------------------------")
#math.erf() : hata fonksiyonu (error function) hesaplar
print(f"Error function of 1: {math.erf(1)}")
print("-------------------------------")
#math.expm1() : e üzeri x - 1 hesaplar
print(f"e to the power of 2 minus 1: {math.expm1(2)}")
print("-------------------------------")
#math.exp2() : 2 üzeri x hesaplar
print(f"2 to the power of 3: {math.exp2(3)}")
print("-------------------------------")
#math.fabs() : sayının mutlak değerini alır
print(f"Absolute value of -5.5: {math.fabs(-5.5)}")
print("-------------------------------")
#math.factorial() : sayının faktöriyelini alır
print(f"Factorial of 5: {math.factorial(5)}")
#math.fmod() : sayının bölümünden kalanı alır
print(f"Fmod of 10 divided by 3: {math.fmod(10, 3)}")
print("-------------------------------")
#math.frexp() : sayıyı mantissa ve exponent olarak döndürür
mantissa, exponent = math.frexp(8)
print(f"Frexp of 8: mantissa={mantissa}, exponent={exponent}")
print("-------------------------------")
#math.fsum() : iterable içindeki sayıları toplar ve daha doğru sonuç verir
numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(f"Sum of numbers using fsum: {math.fsum(numbers)}")
print("-------------------------------")
#math.gamma() : sayının gamma fonksiyonunu hesaplar
print(f"Gamma of 5: {math.gamma(5)}")
print("-------------------------------")
#mathlgamma() : sayının log gamma fonksiyonunu hesaplar
print(f"Log gamma of 5: {math.lgamma(5)}")
print("-------------------------------")
#math.prod() : iterable içindeki sayıların çarpımını alır
numbers = [1, 2, 3, 4, 5]
print(f"Product of numbers: {math.prod(numbers)}")
print("-------------------------------")
#math.gcd() : iki sayının en büyük ortak bölenini hesaplar
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")
print("-------------------------------")
#math.hypot() : dik üçgenin hipotenüsünü hesaplar
print(f"Hypotenuse of sides 3 and 4: {math.hypot(3, 4)}")
print("-------------------------------")
#math.isclose() : iki sayının birbirine yakın olup olmadığını kontrol eder
print(f"Is 0.1 + 0.2 close to 0.3? {math.isclose(0.1 + 0.2, 0.3)}")
print("-------------------------------")
#sayının durum kontrol metodları ile ilgili örnekler
#math.isfinite() : sayının sonlu olup olmadığını kontrol eder
print(f"Is 5 finite? {math.isfinite(5)}")
print("-------------------------------")
#math.isinf() : sayının sonsuz olup olmadığını kontrol eder
print(f"Is infinity infinite? {math.isinf(math.inf)}")
print("-------------------------------")
#math.isnan() : sayının NaN (Not a Number) olup olmadığını kontrol eder
print(f"Is NaN NaN? {math.isnan(math.nan)}")
print("-------------------------------")
#math.Idexp() : sayının 2 üzeri x ile çarpılmış halini döndürür
print(f"ldexp of 3 and 4: {math.ldexp(3, 4)}")
print("-------------------------------")
#math.log() : sayının logaritmasını alır
print(f"Logarithm of 1000 with base 10: {math.log(1000, 10)}")
print("-------------------------------")
#finish





