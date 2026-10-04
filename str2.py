#modify string & escape characters
text = "merhaba"
text1 = "dünya"
print(text + " " + text1)
#UPPPER 
print(text.upper())
#LOWER
print(text.lower())
#REPLACE
print(text.replace("merhaba", "selam"))
#strip 
#strip() METODU, BİR STRINGİN BAŞINDA VEYA SONUNDAKİ BOŞLUKLARI KALDIRMAK İÇİN KULLANILIR. ÖRNEĞİN, text.strip() İLE text STRINGİNİN BAŞINDA VEYA SONUNDAKİ BOŞLUKLARI KALDIRABİLİRİZ.
text2 = "   merhaba dünya   "
print(text2.strip())
#split
#split() METODU, BİR STRINGİ BELİRLİ BİR AYIRICIYA GÖRE BÖLMEK İÇİN KULLANILIR. ÖRNEĞİN, text.split() İLE text STRINGİNİ BOŞLUKLARA GÖRE BÖLEBİLİRİZ.
print(text2.split(","))
#escape characters 
text5 = "merhaba\n dünya"
print(text5)
# \n karakteri, bir satır aşağı geçmek için kullanılır.
#\ karakteri, bir sonraki karakterin özel bir anlamı olmadığını belirtmek için kullanılır. Örneğin, \n karakteri bir satır aşağı geçmek için kullanılırken, \\n karakteri ise \n karakterinin kendisini ifade eder.
print("merhaba\\n dünya")
# \r karakteri, bir satır başına dönmek için kullanılır. Örneğin, \r karakteri bir satır başına dönmek için kullanılırken, \r\n karakteri ise bir satır başına dönmek ve bir satır aşağı geçmek için kullanılır.
print("merhaba\r dünya")
# \t karakteri, bir tab boşluğu bırakmak için kullanılır. Örneğin, \t karakteri bir tab boşluğu bırakmak için kullanılırken, \\t karakteri ise \t karakterinin kendisini ifade eder.
print("merhaba\t dünya")
#\b karakteri, bir karakter geri gitmek için kullanılır. Örneğin, \b karakteri bir karakter geri gitmek için kullanılırken, \\b karakteri ise \b karakterinin kendisini ifade eder.
print("merhaba\b dünya")
#count metodu, bir stringin içinde belirli bir karakterin kaç kez geçtiğini saymak için kullanılır. Örneğin, text.count("a") ifadesi, text stringinde "a" karakterinin kaç kez geçtiğini döndürür.
text = "merhaba dünya"
print(text.count("a"))
result = text.count("a", 0, 10)  # 0'dan 10'a kadar olan karakterler arasında "a" karakterinin sayısını döndürür.
print(result)   
#startswith metodu, bir stringin belirli bir karakterle başlayıp başlamadığını kontrol etmek için kullanılır. Örneğin, text.startswith("mer") ifadesi, text stringinin "mer" ile başlayıp başlamadığını kontrol eder ve True veya False döndürür.
print(text.startswith("mer"))
#endswith metodu, bir stringin belirli bir karakterle bitip bitmediğini kontrol etmek için kullanılır. Örneğin, text.endswith("ya") ifadesi, text stringinin "ya" ile bitip bitmediğini kontrol eder ve True veya False döndürür.
print(text.endswith("ya"))
result = text.endswith("ya", 0, 10)  # 0'dan 10'a kadar olan karakterler arasında "ya" ile bitip bitmediğini kontrol eder.
print(result)
#expandtabs metodu, bir stringdeki tab karakterlerini belirli bir sayıda boşluk karakteri ile değiştirmek için kullanılır. Örneğin, text.expandtabs(4) ifadesi, text stringindeki tab karakterlerini 4 boşluk karakteri ile değiştirir.
text9 = "merhaba\t dünya"
print(text9.expandtabs(4))                                                   
#find metodu, bir stringin içinde belirli bir karakterin ilk geçtiği konumu bulmak için kullanılır. Örneğin, text.find("a") ifadesi, text stringinde "a" karakterinin ilk geçtiği konumu döndürür. Eğer karakter bulunamazsa -1 döndürür.
print(text.find("a"))
result = text.find("a", 0, 10)  # 0'dan 10'a kadar olan karakterler arasında "a" karakterinin ilk geçtiği konumu döndürür.
print(result)
#stringlerde index ve find arasında farklar vardır. index metodu, bir karakterin ilk geçtiği konumu bulmak için kullanılır ve eğer karakter bulunamazsa ValueError hatası fırlatır. find metodu ise, bir karakterin ilk geçtiği konumu bulmak için kullanılır ve eğer karakter bulunamazsa -1 döndürür.
metin = "merhaba dünya"
print(metin.index("a"))  # Çıktı: 3
print(metin.find("a"))  # Çıktı: 3
#İSALNUM() METODU, BİR STRINGİN SADECE SAYILARDAN OLUŞUP OLUŞMADIĞINI KONTROL ETMEK İÇİN KULLANILIR. ÖRNEĞİN, text.isalnum() İFADESİ, text STRINGİNİN SADECE SAYILARDAN OLUŞUP OLUŞMADIĞINI KONTROL EDER VE TRUE VEYA FALSE DÖNDÜRÜR.
print(text.isalnum())
#isalpha() metodu, bir stringin sadece harflerden oluşup oluşmadığını kontrol etmek için kullanılır. Örneğin, text.isalpha() ifadesi, text stringinin sadece harflerden oluşup oluşmadığını kontrol eder ve True veya False döndürür.
print(text.isalpha())
#isascii() metodu, bir stringin sadece ASCII karakterlerinden oluşup oluşmadığını kontrol etmek için kullanılır. Örneğin, text.isascii() ifadesi, text stringinin sadece ASCII karakterlerinden oluşup oluşmadığını kontrol eder ve True veya False döndürür.
print(text.isascii())
#isdecimal() metodu, bir stringin sadece ondalık sayılardan oluşup oluşmadığını kontrol etmek için kullanılır. Örneğin, text.isdecimal() ifadesi, text stringinin sadece ondalık sayılardan oluşup oluşmadığını kontrol eder ve True veya False döndürür.
print(text.isdecimal())
print("--------------------------------------")
#format metodu, bir stringin içinde belirli bir formatta veri yerleştirmek için kullanılır. Örneğin, text.format() ifadesi, text stringinin içinde belirli bir formatta veri yerleştirir ve yeni bir string döndürür.
#format metodu 3 farklı şekilde kullanılabilir:
#1. positional arguments
name = "Ali"
age = 25
print("Benim adım {} ve yaşım {}.".format(name, age))
#2. keyword arguments
print("Benim adım {name} ve yaşım {age}.".format(name=name, age=age))
#3. f-string
print(f"Benim adım {name} ve yaşım {age}.")
#4. sayısal formatlama
text2="Benim adım {0} ve yaşım {1}.".format(name, age)              
print(text2)
#formating types
#sola hizalama
text3 = "Benim adım {0:<10} ve yaşım {1:<10}.".format(name, age)  # < işareti sola hizalama için kullanılır.
print(text3)
#sağa hizalama
text4 = "Benim adım {0:>10} ve yaşım {1:>10}.".format(name, age)  # > işareti sağa hizalama için kullanılır.
print(text4)
#ortala hizalama
text5 = "Benim adım {0:^10} ve yaşım {1:^10}.".format(name, age)  # ^ işareti ortala hizalama için kullanılır.
print(text5)
#matematiksel işaretler ile en sola hizalama
# := işareti, bir sayının işaretini en sola hizalamak için kullanılır. Örneğin, text6 = "Benim adım {0:=10} ve yaşım {1:=10}.".format(name, age) ifadesi, name ve age değişkenlerini en sola hizalar.
text6 = "the temperature is {0:=10} and the humidity is {1:=10}.".format(25, 60)
print(text6)
# :+ ve :- işaretleri, bir sayının işaretini göstermek için kullanılır. Örneğin, text7 = "the temperature is {0:+10} and the humidity is {1:-10}.".format(25, 60) ifadesi, name değişkenini + işareti ile ve age değişkenini - işareti ile gösterir.
text7 = "the temperature is {0:+10} and the humidity is {1:-10}.".format(25, 60)
print(text7)
#ondalık sayılar için formatlama
text8 = "the temperature is {0:.2f} and the humidity is {1:.2f}.".format(25.678, 60.123)
print(text8) #sayıdan sonra kaç basamak gösterileceğini belirler. .2f ifadesi, sayının ondalık kısmının 2 basamak gösterileceğini belirtir.
#pozitif ve negatif sayıların önüne boşluk bırakmak için + ve - işaretleri kullanılabilir. Örneğin, text9 = "the temperature is {0:+10} and the humidity is {1:-10}.".format(25.678, 60.123) ifadesi, sayının önüne + ve - işaretlerini ekler.
metin1="sıcaklık{: } ve nem{: }".format(+25.678, -60.123)
print(metin1)
#binlik ayırıcı olarak virgül kullanmak için , işareti kullanılabilir. Örneğin, text10 = "the temperature is {0:,} and the humidity is {1:,}.".format(25678, 60123) ifadesi, sayının binlik ayırıcı olarak virgül kullanmasını sağlar.
text10 = "the temperature is {0:,} and the humidity is {1:,}.".format(256789999999, 60123999999999999999999999)
print(text10)
#veya _ ile de yapabiliriz. Örneğin, text11 = "the temperature is {0:_} and the humidity is {1:_}.".format(25678, 60123) ifadesi, sayının binlik ayırıcı olarak _ kullanmasını sağlar.
text11 = "the temperature is {0:_} and the humidity is {1:_}.".format(256789999999, 60123999999999999999999999)
print(text11)
#binary dönüştürme 
text12 = "the number is {0:b}.".format(25)
print(text12) # sayıyı binary olarak gösterir.
#prefix ve suffix ekleme
text13 = "the number is {0:#b}.".format(25)
print(text13) # sayıyı binary olarak gösterir ve başına 0b ekler.
#ünicode karakterlerini göstermek için \u ve \U kullanılır. Örneğin, text14 = "the character is {0:\u03A9}.".format(937) ifadesi, sayının unicode karakterini gösterir.
print("119 sayısının karakteri {:c}".format(119)) # sayının unicode karakterini gösterir.
#onluk decemal sayıları göstermek için :d kullanılır. Örneğin, text15 = "the number is {0:d}.".format(25) ifadesi, sayıyı onluk decimal olarak gösterir.
text15 = "the number is {0:d}.".format(25)
print(text15)
#bilimsel gösterim için :e kullanılır. Örneğin, text16 = "the number is {0:e}.".format(25) ifadesi, sayıyı bilimsel gösterim olarak gösterir.
text16 = "the number is {0:e}.".format(25)
print(text16)
#ondal8ık sayıları göstermek için :f kullanılır. Örneğin, text17 = "the number is {0:f}.".format(25) ifadesi, sayıyı ondalık sayı olarak gösterir.
text17 = "the number is {0:f}.".format(25.5555555555555555556)
print(text17)
#ondalık sayıları göstermek için :F kullanılır. Örneğin, text18 = "the number is {0:F}.".format(25) ifadesi, sayıyı ondalık sayı olarak gösterir.
text18 = "the number is {0:F}.".format(25000.00000030000)
print(text18)
#nan ve inf değerlerini göstermek için :g ve :G kullanılır. Örneğin, text19 = "the number is {0:g}.".format(float('nan')) ifadesi, sayıyı nan olarak gösterir.
text19 = "the number is {0:g}.".format(float('nan'))
print(text19)
text20 = "the number is {0:G}.".format(float('inf'))
print(text20)
#sekizli sayıları göstermek için :o kullanılır. Örneğin, text21 = "the number is {0:o}.".format(25) ifadesi, sayıyı sekizli sayı olarak gösterir.
text21 = "the number is {0:o}.".format(25)
print(text21)
#onalık sayıları göstermek için :x ve :X kullanılır. Örneğin, text22 = "the number is {0:x}.".format(25) ifadesi, sayıyı onaltılık sayı olarak gösterir.
text22 = "the number is {0:x}.".format(25)
print(text22)
text23 = "the number is {0:X}.".format(25)
print(text23)
#yüzdelik biçimlendirme
text24 = "the number is {0:%}.".format(0.25)
print(text24) # sayıyı yüzdelik biçimlendirme olarak gösterir.
text25 = "the number is {0:.0%}.".format(0.25)
print(text25) # sayıyı yüzdelik biçimlendirme olarak gösterir ve ondalık kısmını göstermez.

