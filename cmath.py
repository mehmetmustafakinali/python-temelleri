#cmath fonksiyonları, karmaşık sayılarla çalışmak için kullanılır. Bu modül, karmaşık sayılarla ilgili matematiksel işlemleri gerçekleştirmek için çeşitli fonksiyonlar sağlar. Örneğin, karmaşık sayıların mutlak değeri, faz açısı, üstel fonksiyonlar ve trigonometrik fonksiyonlar gibi işlemler cmath modülü ile yapılabilir.
#math.log10() : sayının 10 tabanında logaritmasını alır
import cmath

print(f"Logarithm of 1000 with base 10: {cmath.log10(1000)}")
print("-------------------------------")
#math.log1p(x) : sayının 1+x değerinin logaritmasını alır
print(f"Logarithm of 1 + 0.5: {cmath.log1p(0.5)}")
print("-------------------------------")
#math.log2() : sayının 2 tabanında logaritmasını alır
print(f"Logarithm of 8 with base 2: {cmath.log2(8)}")
print("-------------------------------")
#math.perm(n,k) : n elemandan k elemanlı permütasyon sayısını hesaplar
print(f"Permutations of 5 taken 3 at a time: {cmath.perm(5, 3)}")
print("-------------------------------")
#math.prod() : iterable içindeki sayıların çarpımını alır
numbers = [1, 2, 3, 4, 5]
print(f"Product of numbers: {cmath.prod(numbers)}")
#math.pow(x, y) : x üzeri y hesaplar
print(f"2 to the power of 3: {cmath.pow(2, 3)}")
#cmath ile math aralarındaki fark cmath daha kompleks sayılarla çalışmak için kullanılırken, math modülü daha çok reel sayılarla çalışmak için kullanılır. cmath modülü, karmaşık sayılarla ilgili işlemleri gerçekleştirmek için özel fonksiyonlar sağlar ve karmaşık sayılarla ilgili matematiksel hesaplamaları kolaylaştırır.
print("-------------------------------")
#sanal birim (imaginary part) ve gerçek birim (real part) ile ilgili örnekler
complex_number = 3 + 4j
print(f"Real part: {complex_number.real}")  # Output: 3.0
print(f"Imaginary part: {complex_number.imag}")  # Output: 4.0
#cmath modülü sabitleri ile ilgili örnekler
print(f"Pi: {cmath.pi}")  # Output: 3.141592653589793
print(f"E: {cmath.e}")  # Output: 2.718281828459045
#cmath inf ve cmath nan ile ilgili örnekler
print(f"Infinity: {cmath.inf}")  # Output: inf
print(f"NaN: {cmath.nan}")  # Output: nan
#cmath sqrt ile ilgili örnekler
print(f"Square root of 16: {cmath.sqrt(16)}")  # Output: (4+0j)
print(f"Square root of -16: {cmath.sqrt(-16)}")  # Output: 4j
print("-------------------------------")
#trigonometrik fonksiyonlar ile ilgili örnekler
cmath_sin = cmath.sin(cmath.pi / 2)  # sin(π/2) = 1
cmath_cos = cmath.cos(cmath.pi)      # cos(π) = -1
print(f"Sin(π/2): {cmath_sin}")  # Output: (1+0j)
print(f"Cos(π): {cmath_cos}")  # Output: (-1+0j)
print("-------------------------------")
#cmath.asin(z) : z sayısının arcsin değerini hesaplar
z = 0.5
arcsin_z = cmath.asin(z)
print(f"Arcsin of {z}: {arcsin_z}")  # Output: (0.5235987755982989+0j)
#cmath.acos(z) : z sayısının arccos değerini hesaplar
arccos_z = cmath.acos(z)
print(f"Arccos of {z}: {arccos_z}")  # Output: (1.0471975511965979+0j)
#cmath.atan(z) : z sayısının arctan değerini hesaplar
arctan_z = cmath.atan(z)
print(f"Arctan of {z}: {arctan_z}")  # Output: (0.4636476090008061+0j)
print("-------------------------------")
#cmath.exp(z) : z sayısının üstel değerini hesaplar
exp_z = cmath.exp(z)
print(f"Exponential of {z}: {exp_z}")  # Output: (1.6487212707001282+0j)
#cmath.log(z) : z sayısının doğal logaritmasını hesaplar
log_z = cmath.log(z)
print(f"Natural logarithm of {z}: {log_z}")  # Output: (-0.6931471805599453+0j)
#durum denetim 
#cmath.isfinite(z) : z sayısının sonlu olup olmadığını kontrol eder
is_finite = cmath.isfinite(z)
print(f"Is {z} finite? {is_finite}")  # Output: True
print("-------------------------------")
#cmath.isinf(z) : z sayısının sonsuz olup olmadığını kontrol eder
is_infinite = cmath.isinf(z)
print(f"Is {z} infinite? {is_infinite}")  # Output: False
print("-------------------------------")
#cmath.isnan(z) : z sayısının NaN (Not a Number) olup olmadığını kontrol eder
is_nan = cmath.isnan(z)
print(f"Is {z} NaN? {is_nan}")  # Output: False
print("-------------------------------")
#cmath.isclose(a, b) : a ve b sayılarının birbirine yakın olup olmadığını kontrol eder
a = 0.1 + 0.2
b = 0.3
is_close = cmath.isclose(a, b)
print(f"Is {a} close to {b}? {is_close}")  # Output: True
#cmath.phase(z) : z sayısının faz açısını hesaplar
phase_z = cmath.phase(z)
print(f"Phase of {z}: {phase_z}")  # Output: 0.0
print("-------------------------------")
#cmhath.polar(z) : z sayısının kutupsal koordinatlarını hesaplar
polar_z = cmath.polar(z)
print(f"Polar coordinates of {z}: {polar_z}")  # Output: (0.5, 0.0)
#cmaht.sqrt(z) : z sayısının karekökünü hesaplar
sqrt_z = cmath.sqrt(z)
print(f"Square root of {z}: {sqrt_z}")  # Output: (0.7071067811865476+0j)
print("-------------------------------")
#cmath.rect(r, phi) : kutupsal koordinatları dikdörtgen koordinatlara dönüştürür
rect_z = cmath.rect(1, cmath.pi / 4)  # r=1, phi=π/4
print(f"Rectangular coordinates of (1, π/4): {rect_z}")
print("-------------------------------")
#cmath.log10(z) : z sayısının 10 tabanında logaritmasını hesaplar
log10_z = cmath.log10(z)
print(f"Logarithm of {z} with base 10: {log10_z}")  # Output: (-0.3010299956639812+0j)
print("-------------------------------")
