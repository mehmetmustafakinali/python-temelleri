#datetime modülü: tarih ve saat ile ilgili işlemleri yapmamızı sağlayan modüldür.
import datetime
#şu anki tarih ve zaman 
now = datetime.datetime.now()
print(now)
#veya sadece tarihi almak için
today = datetime.date.today()
print(today)
#tarih nesnelerini birleştirme ve veri tiplemeleri 
date1 = datetime.date(2023, 10, 1)
date2 = datetime.date(2023, 10, 15)
print(date1, date2)
#haftanın günü ve detaylı biçimlendirme metodları
print(now.weekday())  # Output: 0 (Monday)
#strftime() metodu ile tarih ve saat biçimlendirme
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2023-10-01 12:34:56
print(now.strftime("%A, %B %d, %Y"))  # Output: Sunday, October 01, 2023
print(now.strftime("%I:%M %p"))  # Output: 12:34 PM
print(now.strftime("%Y-%m-%d %H:%M:%S.%f"))  # Output: 2023-10-01 12:34:56.123456
print(now.strftime("%Y-%m-%d %H:%M:%S %Z"))  # Output: 2023-10-01 12:34:56 UTC
print(now.strftime("%Y-%m-%d %H:%M:%S %z"))  # Output: 2023-10-01 12:34:56 +0000
print(now.strftime("%Y-%m-%d %H:%M:%S %Z%z"))  # Output: 2023-10-01 12:34:56 UTC+0000
print(now.strftime("%Y-%m-%d %H:%M:%S %Z%z"))  # Output: 2023-10-01 12:34:56 UTC+0000
print("-------------------------------")
#ctime() metodu ile tarih ve saat biçimlendirme
print(now.ctime())  # Output: Sun Oct  1 12:34:56 2023
print(now.isoformat())  # Output: 2023-10-01T12:34:56.123456
print("-------------------------------")
# %a ve %A: haftanın gününü kısa ve uzun biçimde gösterir.
print(now.strftime("%a"))  # Output: Sun
print(now.strftime("%A"))  # Output: Sunday
print("-------------------------------")
# %b ve %B: ayın adını kısa ve uzun biçimde gösterir.
print(now.strftime("%b"))  # Output: Oct
print(now.strftime("%B"))  # Output: October
print("-------------------------------")
# %d: ayın gününü gösterir (01-31).
print(now.strftime("%d"))  # Output: 01
print("-------------------------------")
# %m: ayı gösterir (01-12).
print(now.strftime("%m"))  # Output: 10
print("-------------------------------")
# %Y: yılı gösterir (4 haneli).
print(now.strftime("%Y"))  # Output: 2023
print("-------------------------------")
# %H: saati 24 saat formatında gösterir (00-23).
print(now.strftime("%H"))  # Output: 12
print("-------------------------------")
# %M: dakikayı gösterir (00-59).
print(now.strftime("%M"))  # Output: 34
print("-------------------------------")
# %S: saniyeyi gösterir (00-59).
print(now.strftime("%S"))  # Output: 56
print("-------------------------------")
# %f: mikrosaniyeyi gösterir (000000-999999).
print(now.strftime("%f"))  # Output: 123456
print("-------------------------------")
# %p: AM veya PM'yi gösterir.
print(now.strftime("%p"))  # Output: PM
print("-------------------------------")
# %Z: zaman dilimini gösterir (örn. UTC, EST).
print(now.strftime("%Z"))  # Output: UTC
print("-------------------------------")
# %z: zaman dilimini gösterir (örn. +0000, -0500).
print(now.strftime("%z"))  # Output: +0000
print("-------------------------------")
# %j: yılın gününü gösterir (001-366).
print(now.strftime("%j"))  # Output: 274
print("-------------------------------")
# %U: yılın haftasını gösterir (00-53, Pazar günü başlar).
print(now.strftime("%U"))  # Output: 39
print("-------------------------------")
# %W: yılın haftasını gösterir (00-53, Pazartesi günü başlar).
print(now.strftime("%W"))  # Output: 39
print("-------------------------------")
# strftime() metodu ile tarih ve saat biçimlendirme
#unix zaman damgası (timestamp) ile ilgili örnek
timestamp = now.timestamp()
print(timestamp)  # Output: 1696150496.123456
print("-------------------------------")
#timedelta ile tarih ve saat hesaplamaları
delta = datetime.timedelta(days=5, hours=3, minutes=30)
print(delta)  # Output: 5 days, 3:30:00
print("-------------------------------")
#gün ekleme gün çıkartma işlemleri
new_date = now + datetime.timedelta(days=5)
print(new_date)  # Output: 2023-10-06 15:04:56.123456
print("-------------------------------")
#saat ve dakika ekleme çıkartma işlemeleri 
new_time = now + datetime.timedelta(hours=2, minutes=15)
print(new_time)  # Output: 2023-10-01 17:19:56.123456
print("-------------------------------")
#iso takvim bilgisi 
print(now.isocalendar())  # Output: (2023, 39, 5)
#yanlızca tarih ve zaman nesenleri : date , time ve combine() 
date_only = now.date()
print(date_only)  # Output: 2023-10-01
time_only = now.time()
print(time_only)  # Output: 12:34:56.123456
print("-------------------------------")
#tarih nesenleri ile ilgili örnekler
#replace() metodu: tarih nesnesinin belirli bir bileşenini değiştirir.
new_date = now.replace(year=2024, month=12, day=25)
print(new_date)  # Output: 2024-12-25 12:34:56.123456
print("-------------------------------")
#date() metodu: tarih nesnesi oluşturur.
date_obj = datetime.date(2023, 10, 1)
print(date_obj)  # Output: 2023-10-01
print("-------------------------------")
#time() metodu: saat nesnesi oluşturur.
time_obj = datetime.time(14, 30, 0)
print(time_obj)  # Output: 14:30:00
print("-------------------------------")
#bağımsız time modülleri ile ilgili örnekler
time_obj = datetime.time(14, 30, 0)
print(time_obj)  # Output: 14:30:00
print(time_obj.hour)  # Output: 14
print(time_obj.minute)  # Output: 30
print(time_obj.second)  # Output: 0
