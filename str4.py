#ord() ne işe yarar? ord() metodu, bir karakterin Unicode kod noktasını döndürür. Örneğin, "A" karakterinin Unicode kod noktası 65'tir. Bu nedenle, ord("A") ifadesi 65 döndürür.
#örnek 1
print(ord("A"))  # Çıktı: 65
#chr() metodu, bir Unicode kod noktasını karaktere dönüştürür. Örneğin, 65 sayısı "A" karakterine karşılık gelir. Bu nedenle, chr(65) ifadesi "A" döndürür.
#örnek 2
print(chr(65))  # Çıktı: A
#bin() metodu, bir sayıyı ikili (binary) sayı sistemine dönüştürür. Örneğin, 10 sayısı ikili sayı sisteminde 1010 olarak temsil edilir. Bu nedenle, bin(10) ifadesi '0b1010' döndürür.
#örnek 3
print(bin(10))  # Çıktı: 0b1010
#pythonda karakter kodlama hatası türkçe karakterler için oluşabilir. Bu hatayı önlemek için dosyanın başına aşağıdaki satırı ekleyebilirsiniz:
# -*- coding: utf-8 -*-
metin = "ç"
try: 
    print(ord(metin))
except UnicodeEncodeError:
    print("UnicodeEncodeError: Türkçe karakterler için kodlama hatası oluştu.")
#********************************************************************************
# Ş GİB TÜRKÇE KARAKTERLERİN UNICODE KOD NOKTALARI
print(ord("Ş"))  # Çıktı: 350
print(ord("Ğ"))  # Çıktı: 286
#YANİ BUNLAR 2 BYTE KARAKTERLERDİR. BU YÜZDEN BAZI DURUMLARDA KODLAMA HATASI OLUŞABİLİR.
#**************************
#encoding ve decoding işlemleri
metin="python"
#metini utf-8 formatında encode edelim
bytes_metin = metin.encode("utf-8")
print(bytes_metin)  # Çıktı: b'python'
print(type(bytes_metin))  # Çıktı: <class 'bytes'>
#bytes_metin değişkenini tekrar decode edelim
decoded_metin = bytes_metin.decode("utf-8")
print(decoded_metin)  # Çıktı: python
#encode içinddeki hata yönetimi
#strict, ignore, replace, xmlcharrefreplace, backslashreplace, namereplace
#strict: Hata oluştuğunda bir UnicodeEncodeError istisnası fırlatır. Bu, varsayılan davranıştır.
#ignore: Hatalı karakterleri yoksayar ve onları atlar. Bu, hatalı karakterleri tamamen yok sayar ve çıktıda görünmezler.
#replace: Hatalı karakterleri yerine bir yer tutucu karakter (genellikle '?') ile değiştirir. Bu, hatalı karakterleri belirgin bir şekilde işaretler.
#xmlcharrefreplace: Hatalı karakterleri XML karakter referansları ile değiştirir. Bu, hatalı karakterleri XML uyumlu bir şekilde temsil eder.
#backslashreplace: Hatalı karakterleri ters eğik çizgi ile değiştirir. Bu, hatalı karakterleri bir ters eğik çizgi ve karakter kodu ile temsil eder.
#namereplace: Hatalı karakterleri, karakter adları ile değiştirir. Bu, hatalı karakterleri bir karakter adı ile temsil eder.
#örnek 1
metin = "ç"
try:
    bytes_metin = metin.encode("ascii", "strict")
    print(bytes_metin)
except UnicodeEncodeError:
    print("UnicodeEncodeError: 'ascii' codec can't encode character 'ç' in position 0: ordinal not in range(128)")
    bytes_metin = metin.encode("ascii", "ignore")
    print(bytes_metin)
    bytes_metin = metin.encode("ascii", "replace")
    print(bytes_metin)
    bytes_metin = metin.encode("ascii", "xmlcharrefreplace")
    print(bytes_metin)
    bytes_metin = metin.encode("ascii", "backslashreplace")
    print(bytes_metin)
    bytes_metin = metin.encode("ascii", "namereplace")
    print(bytes_metin)