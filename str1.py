#stringler  
print("merhaba" + " " + "dünya")
#çoklu stringler 
text = """merhaba
dünya"""
print(text)
#STRİNGLER BİRER ARRAY GİBİ DÜŞÜNÜLEBİLİR. ÖRNEĞİN, BİR STRINGİN İÇİNDEKİ HER KARAKTERE İNDİS İLE ERİŞİLEBİLİR. ÖRNEĞİN, text[0] İLK KARAKTERİ, text[1] İKİNCİ KARAKTERİ VERSA.
#BUNU ŞU ŞEKİLDE YAPABİLİRİZ:
print(text[0])
#LEN FONKSİYONU İLE BİR STRINGİN UZUNLUĞUNU ÖĞRENEBİLİRİZ. ÖRNEĞİN, len(text) İLE text STRINGİNİN UZUNLUĞUNU ÖĞRENEBİLİRİZ.
print(len(text))
#İN FONKSİYONU İLE BİR STRINGİN İÇİNDE BELİRLİ BİR KARAKTERİN VARLIĞINI KONTROL EDEBİLİRİZ. ÖRNEĞİN, "merhaba" IN text İLE text STRINGİNİN İÇİNDE "merhaba" KARAKTERLERİNİN VARLIĞINI KONTROL EDEBİLİRİZ.
print("merhaba" in text)    
#NOT İN İSE BİR STRINGİN İÇİNDE BELİRLİ BİR KARAKTERİN OLMADIĞINI KONTROL EDER. ÖRNEĞİN, "merhaba" NOT IN text İLE text STRINGİNİN İÇİNDE "merhaba" KARAKTERLERİNİN OLMADIĞINI KONTROL EDEBİLİRİZ.
print("merhaba" not in text)
print("----------------------------------------------------------------" \
"")
#stringlerde dilimleme işlemi yapılabilir. Örneğin, text[0:5] ile text STRINGİNİN İLK 5 KARAKTERİNİ ALABİLİRİZ. VEYA text[5:] İLE text STRINGİNİN 5. KARAKTERİNDEN SONRASINI ALABİLİRİZ. VEYA text[:5] İLE text STRINGİNİN İLK 5 KARAKTERİNİ ALABİLİRİZ.
print(text[0:5])
print(text[5:])
print(text[:5])
#string birleştirme işlemi yapılabilir. Örneğin, text1 + text2 ile text1 VE text2 STRINGLERİNİ BİRLEŞTİREBİLİRİZ.
text1 = "merhaba"
text2 = "dünya"
print(text1 + " " + text2)


