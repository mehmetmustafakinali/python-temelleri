#pythonda istatistik modülü 
#statistics.harmonic_mean() : sayısal değerlerin harmonik ortalamasını hesaplar
import statistics
data = [1, 2, 3, 4, 5]
harmonic_mean = statistics.harmonic_mean(data)
print(f"Harmonic mean of {data}: {harmonic_mean}")  # Output: 2.18978102189781
#statistics.median() : sayısal değerlerin medyanını hesaplar
print("-------------------------------")
median_value = statistics.median(data)
print(f"Median of {data}: {median_value}")  # Output: 3
#statistics.median_low() : sayısal değerlerin medyanını hesaplar (düşük medyan)
print("-------------------------------")
median_low_value = statistics.median_low(data)
print(f"Median low of {data}: {median_low_value}")  # Output: 3
#statistics.median_high() : sayısal değerlerin medyanını hesaplar (yüksek medyan)
print("-------------------------------")
median_high_value = statistics.median_high(data)
print(f"Median high of {data}: {median_high_value}")  # Output: 3
print("-------------------------------")
#statistics.median_grouped() : sayısal değerlerin gruplandırılmış medyanını hesaplar
grouped_data = [1, 2, 2, 3, 4, 5]
median_grouped_value = statistics.median_grouped(grouped_data)
print(f"Median grouped of {grouped_data}: {median_grouped_value}")  # Output: 2.5
print("-------------------------------")
#statistics.median_grouped() : sayısal değerlerin gruplandırılmış medyanını hesaplar
grouped_data = [1, 2, 2, 3, 4, 5]
median_grouped_value = statistics.median_grouped(grouped_data)
print(f"Median grouped of {grouped_data}: {median_grouped_value}")  # Output: 2.5
print("-------------------------------")
#statistics.median_low() : sayısal değerlerin gruplandırılmış medyanını hesaplar (düşük medyan)
grouped_data = [1, 2, 2, 3, 4, 5]
median_low_grouped_value = statistics.median_low(grouped_data)
print(f"Median low grouped of {grouped_data}: {median_low_grouped_value}")  # Output: 2
print("-------------------------------")
#statistics.median_high() : sayısal değerlerin gruplandırılmış medyanını hesaplar (yüksek medyan)
grouped_data = [1, 2, 2, 3, 4, 5]
median_high_grouped_value = statistics.median_high(grouped_data)
print(f"Median high grouped of {grouped_data}: {median_high_grouped_value}")  # Output: 3
print("-------------------------------")
#statistics.mode() : sayısal değerlerin modunu hesaplar
mode_value = statistics.mode(data)
print(f"Mode of {data}: {mode_value}")  # Output: 1
print("-------------------------------")
#staticstics.multimode() : sayısal değerlerin modlarını hesaplar
multimode_value = statistics.multimode(data)
print(f"Multimode of {data}: {multimode_value}")  # Output: [1, 2, 3, 4, 5]
print("-------------------------------")
#statistics.pstdev() : sayısal değerlerin popülasyon standart sapmasını hesaplar
pstdev_value = statistics.pstdev(data)
print(f"Population standard deviation of {data}: {pstdev_value}")  # Output: 1.4142135623730951
print("-------------------------------")
#statistics.stdev() : sayısal değerlerin örneklem standart sapmasını hesaplar
stdev_value = statistics.stdev(data)
print(f"Sample standard deviation of {data}: {stdev_value}")  # Output: 1.5811388300841898
print("-------------------------------")
#statistics.pvariance() : sayısal değerlerin popülasyon varyansını hesaplar
pvariance_value = statistics.pvariance(data)
print(f"Population variance of {data}: {pvariance_value}")  # Output: 2.0
print("-------------------------------")
#statistics.variance() : sayısal değerlerin örneklem varyansını hesaplar
variance_value = statistics.variance(data)
print(f"Sample variance of {data}: {variance_value}")  # Output: 2.5
print("-------------------------------")
