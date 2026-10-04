# 🐍 Python Temelleri: Sıfırdan İleri Seviyeye Kapsamlı Rehber

<p align="center">
  <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Python-Dark.svg" alt="Python" width="100" height="100" />
</p>

<p align="center">
  <strong>Modern, anlaşılır ve uygulamalı kod örnekleriyle Nesne Yönelimli Programlama'ya (OOP) kadar tüm Python temellerini kapsayan eksiksiz başvuru kaynağı.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Versiyonu" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Lisans-MIT-green.style=for-the-badge?style=for-the-badge" alt="Lisans" /></a>
  <img src="https://img.shields.io/github/repo-size/mehmetmustafakinali/python-temelleri?style=for-the-badge&color=orange" alt="Repo Boyutu" />
  <img src="https://img.shields.io/github/stars/mehmetmustafakinali/python-temelleri?style=for-the-badge&color=yellow" alt="Yıldızlar" />
  <img src="https://img.shields.io/github/forks/mehmetmustafakinali/python-temelleri?style=for-the-badge&color=blue" alt="Forklar" />
</p>

<p align="center">
  ⭐ <b>Projeyi beğendiyseniz sağ üst köşeden yıldız (Star) vererek destekleyebilirsiniz!</b> ⭐
</p>

---

## 📑 İçindekiler

- [Hakkında](#-hakkında)
- [Neden Bu Repo?](#-neden-bu-repo)
- [📂 Dosya ve Konu Haritası](#-dosya-ve-konu-haritası)
- [🧠 A'dan Z'ye Konu Özetleri ve Hile Kartları (Cheatsheet)](#-adan-zye-konu-özetleri-ve-hile-kartları-cheatsheet)
  - [1. Değişkenler ve Veri Tipleri](#1-değişkenler-ve-veri-tipleri)
  - [2. Operatörler Dünyası](#2-operatörler-dünyası)
  - [3. String (Metin) Manipülasyonu](#3-string-metin-manipülasyonu)
  - [4. Veri Yapıları Kıyaslama Tablosu](#4-veri-yapıları-kıyaslama-tablosu)
  - [5. Koşul İfadeleri ve Döngüler](#5-koşul-ifadeleri-ve-döngüler)
  - [6. Fonksiyonlar, Lambda ve İleri Düzey Kavramlar](#6-fonksiyonlar-lambda-ve-ileri-düzey-kavramlar)
  - [7. Python Decorator Mimarisi](#7-python-decorator-mimarisi)
  - [8. Yerleşik (Built-in) Modüller](#8-yerleşik-built-in-modüller)
- [🚀 OOP'ye (Nesne Yönelimli Programlama) Geçiş](#-oopye-nesne-yönelimli-programlama-geçiş)
- [💻 Kurulum ve Çalıştırma](#-kurulum-ve-çalıştırma)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)
- [📄 Lisans](#-lisans)

---

## 📌 Hakkında

Bu depo, Python programlama dilini öğrenmek isteyen geliştiriciler, öğrenciler ve bilgilerini tazelemek isteyen profesyoneller için hazırlanmış **interaktif ve açıklamalı bir kod kütüphanesidir**.

İlk kod olan `helloworld.py` dosyasından başlayıp, `Decorator`, `Lambda`, `İleri Seviye Veri Yapıları` ve standart kütüphane modüllerine (`cmath`, `datetime`, `statistics`, `random`, `math`) kadar uzanan geniş bir müfredatı kapsar.

---

## 🌟 Neden Bu Repo?

- 🎯 **Açıklayıcı Kodlar:** Her dosya salt kod yerine, satır içi açıklamalar ve çıktılar içerir.
- ⚡ **Hızlı Başvuru (Cheatsheet):** İhtiyacınız olan bir metodu (ör. `list.pop()`, `str.find()`, `*args/**kwargs`) anında bulabilirsiniz.
- 🏗️ **Sağlam Temel:** Nesne Yönelimli Programlama'ya (OOP) geçmeden önce öğrenilmesi gereken her konuyu eksiksiz ele alır.
- 🧪 **Pratik Örnekler:** Gerçek hayat senaryoları ve algoritmik egzersizlerle pekiştirilmiştir.

---

## 📂 Dosya ve Konu Haritası

| No | Dosya Adı | Kategori | Açıklama | Seviye |
|:---|:---|:---|:---|:---:|
| 1 | [`helloworld.py`](./helloworld.py) | Temel | `print()`, kaçış dizileri (`\n`, `\t`), ilk adımlar | 🟢 Başlangıç |
| 2 | [`veriableler.py`](./veriableler.py) | Temel | Değişken tanımlama kuralları, hafıza yönetimi | 🟢 Başlangıç |
| 3 | [`type.py`](./type.py) | Veri Tipleri | `type()`, tip dönüşümleri (`int`, `float`, `str`, `bool`) | 🟢 Başlangıç |
| 4 | [`operatoler.py`](./operatoler.py) | Operatörler | Aritmetik (`+`, `-`, `*`, `/`, `//`, `%`, `**`) ve atama operatörleri | 🟢 Başlangıç |
| 5 | [`karşılaştırmaoperatorleri.py`](./karşılaştırmaoperatorleri.py) | Operatörler | `==`, `!=`, `<`, `>`, `<=`, `>=` mantıksal kontrolleri | 🟢 Başlangıç |
| 6 | [`bitselaramaoperatorleri.py`](./bitselaramaoperatorleri.py) | Operatörler | Bit seviyesinde işlemler (`&`, `\|`, `^`, `~`, `<<`, `>>`) | 🟡 Orta |
| 7 | [`uyelikoperatorleri.py`](./uyelikoperatorleri.py) | Operatörler | Kimlik (`is`, `is not`) ve üyelik (`in`, `not in`) işlemleri | 🟢 Başlangıç |
| 8 | [`str1.py`](./str1.py) | String | String tanımlama, indexleme ve parçalama (slicing) | 🟢 Başlangıç |
| 9 | [`str2.py`](./str2.py) | String | Büyük/küçük harf dönüşümleri, arama metotları (`find`, `index`) | 🟢 Başlangıç |
| 10 | [`str3.py`](./str3.py) | String | Kırpma (`strip`), birleştirme (`join`), ayırma (`split`) işlemleri | 🟡 Orta |
| 11 | [`str4.py`](./str4.py) | String | String formatlama yöntemleri (`f-string`, `.format()`, `%`) | 🟡 Orta |
| 12 | [`kosulluifadelergiriş.py`](./kosulluifadelergiriş.py) | Kontrol Akışı | `if`, `else` blokları ve `bool` karar mekanizmaları | 🟢 Başlangıç |
| 13 | [`koşulluifadeler.py`](./koşulluifadeler.py) | Kontrol Akışı | İç içe koşullar (Nested if), `elif` zincirleri | 🟢 Başlangıç |
| 14 | [`while.py`](./while.py) | Döngüler | `while` döngüsü, sonsuz döngüler, sayaç yönetimi | 🟢 Başlangıç |
| 15 | [`for.py`](./for.py) | Döngüler | `for` döngüsü, `range()`, `break`, `continue`, `pass` | 🟢 Başlangıç |
| 16 | [`list.py`](./list.py) | Veri Yapıları | Listeler, CRUD işlemleri ve tüm liste metotları | 🟢 Başlangıç |
| 17 | [`listdongu.py`](./listdongu.py) | Veri Yapıları | Döngülerle liste manipülasyonu ve List Comprehension | 🟡 Orta |
| 18 | [`tuplegiris.py`](./tuplegiris.py) | Veri Yapıları | Demetler (Tuple), immutability, unpacking kuralları | 🟢 Başlangıç |
| 19 | [`setgiriş.py`](./setgiriş.py) | Veri Yapıları | Kümeler (Set), kesişim, birleşim, fark ve simetrik fark | 🟡 Orta |
| 20 | [`Dictionary.py`](./Dictionary.py) | Veri Yapıları | Sözlükler (Dictionary), Key-Value mantığı, `.items()`, `.get()` | 🟡 Orta |
| 21 | [`function.py`](./function.py) | Fonksiyonlar | Fonksiyon anatomisi, `return`, parametreler, default argümanlar | 🟡 Orta |
| 22 | [`function_example.py`](./function_example.py) | Fonksiyonlar | `*args`, `**kwargs`, Scope kuralları (Local/Global) | 🟡 Orta |
| 23 | [`lambda_func.py`](./lambda_func.py) | Fonksiyonlar | İsimsiz fonksiyonlar (`lambda`), `map()`, `filter()`, `reduce()` | 🟡 Orta |
| 24 | [`decorator.py`](./decorator.py) | İleri Seviye | Fonksiyon sarıcılar, `@decorator` sözdizimi, yetkilendirme & süre ölçümü | 🔴 İleri |
| 25 | [`math_func.py`](./math_func.py) | Modüller | Standart `math` modülü (Trigonometri, logaritma, faktöriyel) | 🟢 Başlangıç |
| 26 | [`cmath.py`](./cmath.py) | Modüller | Karmaşık sayılar matematiği (`cmath` modülü) | 🟡 Orta |
| 27 | [`random.py`](./random.py) | Modüller | Rastgele sayı üretimi, liste karıştırma, rastgele seçim | 🟢 Başlangıç |
| 28 | [`datetime_modülü.py`](./datetime_modülü.py) | Modüller | Tarih-saat işlemleri, `strftime`, `timedelta`, zaman farkı | 🟡 Orta |
| 29 | [`istatistik_modülü.py`](./istatistik_modülü.py) | Modüller | İstatistik modülü (`mean`, `median`, `mode`, `stdev`, `variance`) | 🟡 Orta |
| 30 | [`example.py`](./example.py) | Pratik | Algoritmik problem çözümleri ve pekiştirme uygulamaları | 🟡 Orta |
| 31 | [`slexample.py`](./slexample.py) | Pratik | Dilimleme ve string alıştırmaları | 🟢 Başlangıç |

---

## 🧠 A'dan Z'ye Konu Özetleri ve Hile Kartları (Cheatsheet)

### 1. Değişkenler ve Veri Tipleri

Python dinamik tipli (dynamically typed) bir dildir. Tip belirtmenize gerek kalmadan değer atayabilirsiniz:

```python
x = 10          # int (Tam sayı)
pi = 3.14       # float (Ondalıklı sayı)
dil = "Python"  # str (Metin)
aktif = True    # bool (Doğru / Yanlış)
kompleks = 2+3j # complex (Karmaşık sayı)

# Tip Dönüşümü (Type Casting)
yas = int("25")       # str -> int
oran = float(10)      # int -> float (10.0)
durum = bool(1)       # int -> bool (True)
metin = str(123)      # int -> str ("123")
```

---

### 2. Operatörler Dünyası

| Operatör Türü | Örnekler | Anlamı |
|:---|:---|:---|
| **Aritmetik** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Toplama, Çıkarma, Çarpma, Bölme, Taban Bölme, Mod, Üs |
| **Atama** | `=`, `+=`, `-=`, `*=`, `/=` | Değere işlem yapıp tekrar aynı değişkene atama |
| **Karşılaştırma** | `==`, `!=`, `>`, `<`, `>=`, `<=` | Eşit mi, Eşit değil mi, Büyüktür, Küçüktür vb. |
| **Mantıksal** | `and`, `or`, `not` | Ve, Veya, Değil mantığı |
| **Üyelik** | `in`, `not in` | Koleksiyon içinde eleman var mı kontrolü |
| **Kimlik** | `is`, `is not` | Bellek adreslerinin (id) aynı nesneye işaret edip etmediği |
| **Bitsel (Bitwise)**| `&`, `\|`, `^`, `~`, `<<`, `>>` | Sayıların ikili (binary) düzeyinde işlenmesi |

```python
# Kimlik ve Üyelik Örneği:
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)    # True (Değerler aynı)
print(a is b)    # False (Farklı bellek adresleri)
print(2 in a)    # True (2 elemanı a listesinde var)
```

---

### 3. String (Metin) Manipülasyonu

Python'da stringler **immutable** (değiştirilemez) karakter dizileridir.

```python
metin = "Python Programlama Dili"

# Dilimleme (Slicing): [başlangıç : bitiş : adım]
print(metin[0:6])    # "Python"
print(metin[::-1])   # "iliD amalmargorP nohtyP" (Ters çevirme)

# En Çok Kullanılan Metotlar:
metin.lower()        # Tümünü küçük harf yapar
metin.upper()        # Tümünü büyük harf yapar
metin.strip()        # Baş ve sondaki boşlukları temizler
metin.replace("P", "J") # Karakter/kelime değiştirir
metin.split(" ")     # Boşluktan bölerek liste yapar
"-".join(["A", "B"]) # Listeyi tire ile birleştirir -> "A-B"

# Modern f-string Formatlama
ad = "Mehmet"
skor = 98.456
print(f"Öğrenci: {ad} | Puan: {skor:.1f}")  # Puan: 98.5
```

---

### 4. Veri Yapıları Kıyaslama Tablosu

| Özellik | Liste (`list`) | Demet (`tuple`) | Küme (`set`) | Sözlük (`dict`) |
|:---|:---:|:---:|:---:|:---:|
| **Sözdizimi** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"a": 1, "b": 2}` |
| **Sıralı mı? (Ordered)** | ✅ Evet | ✅ Evet | ❌ Hayır | ✅ Evet (3.7+) |
| **Değiştirilebilir mi? (Mutable)** | ✅ Evet | ❌ Hayır | ✅ Evet | ✅ Evet |
| **Tekrarlayan Eleman? (Duplicate)**| ✅ Evet | ✅ Evet | ❌ Hayır (Benzersiz) | ❌ Anahtarlar Benzersiz |
| **İndekslenebilir mi?** | ✅ Evet | ✅ Evet | ❌ Hayır | ✅ Key ile erişim |
| **Kullanım Amacı** | Dinamik veri grupları | Güvenli, sabit veriler | Matematiksel küme işlemleri | Hızlı arama / Key-Value |

---

### 5. Koşul İfadeleri ve Döngüler

#### Ternary (Tek Satır Koşul)
```python
yas = 20
durum = "Reşit" if yas >= 18 else "Reşit Değil"
```

#### List Comprehension (Kompakt Döngüler)
```python
# 1'den 10'a kadar çift sayıların karesi:
cift_kareler = [x**2 for x in range(1, 11) if x % 2 == 0]
# Çıktı: [4, 16, 36, 64, 100]
```

---

### 6. Fonksiyonlar, Lambda ve İleri Düzey Kavramlar

#### Esnek Parametreler: `*args` ve `**kwargs`
```python
def siparis_ver(musteri, *urunler, **detaylar):
    print(f"Müşteri: {musteri}")
    print(f"Ürünler (Tuple): {urunler}")
    print(f"Detaylar (Dict): {detaylar}")

siparis_ver("Ahmet", "Kitap", "Kalem", kargo="Hızlı", odeme="Kredi Kartı")
```

#### Lambda, Map, Filter
```python
sayilar = [1, 2, 3, 4, 5, 6]

# Çift sayıları filtrele:
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))

# Her sayının 3 katını al:
ucler = list(map(lambda x: x * 3, sayilar))
```

---

### 7. Python Decorator Mimarisi

Decorator'lar, mevcut bir fonksiyonun davranışını fonksiyonun kaynak kodunu değiştirmeden genişletmek için kullanılır (Logging, Kimlik Doğrulama, Zaman Ölçümü):

```python
import time

def sure_olc(fonksiyon):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"[{fonksiyon.__name__}] çalışma süresi: {bitis - baslangic:.6f} sn")
        return sonuc
    return wrapper

@sure_olc
def agır_hesaplama():
    toplam = sum(range(1_000_000))
    return toplam

agır_hesaplama()
```

---

### 8. Yerleşik (Built-in) Modüller

Python zengin bir standart kütüphane ekosistemiyle gelir:

- 🧮 **`math` & `cmath`**: Faktöriyel, logaritma, trigonometri, irrasyonel ve karmaşık sayılar.
- 🎲 **`random`**: `randint()`, `choice()`, `shuffle()`, `sample()`.
- 📅 **`datetime`**: `datetime.now()`, `timedelta` (gün/saat farkı ekleme çıkarma), `strftime` (biçimlendirme).
- 📊 **`statistics`**: `mean` (ortalama), `median` (ortanca), `mode` (en sık geçen), `stdev` (standart sapma).

---

## 🚀 OOP'ye (Nesne Yönelimli Programlama) Geçiş

Bu repoda tamamlanan temel konuların ardından bir sonraki durağınız **Nesne Yönelimli Programlama (OOP)** olacaktır.

### OOP Temel Yapıtaşları:
1. **Class (Sınıf) ve Object (Nesne):** Dünyadaki varlıkların taslakları (`class Araba:`) ve somut örnekleri (`bmw = Araba()`).
2. **Encapsulation (Kapsülleme):** Veriyi ve metotları koruma altına alma (`self.__gizli_veri`).
3. **Inheritance (Kalıtım):** Üst sınıftan özellik miras alma (`class Kopek(Hayvan):`).
4. **Polymorphism (Çok Biçimlilik):** Aynı metot adının farklı sınıflarda farklı davranması.
5. **Abstraction (Soyutlama):** Detayları gizleyip sadece arayüzü sunma (`abc` modülü).

---

## 💻 Kurulum ve Çalıştırma

### 1. Repoyu Klonlayın
```bash
git clone https://github.com/mehmetmustafakinali/python-temelleri.git
cd python-temelleri
```

### 2. Dosyaları Çalıştırın
Sisteminizde Python 3'ün yüklü olduğundan emin olun:
```bash
python --version
```

İstediğiniz herhangi bir konuyu doğrudan çalıştırıp deneyebilirsiniz:
```bash
# Temel string işlemlerini çalıştırmak için:
python str2.py

# Decorator mimarisini test etmek için:
python decorator.py

# İstatistik modülünü test etmek için:
python istatistik_modülü.py
```

---

## 🤝 Katkıda Bulunma

Katkı sağlamak isterseniz çok memnun oluruz!
1. Bu depoyu Fork'layın (`Fork` butonuna basın)
2. Yeni bir Dal (Branch) oluşturun (`git checkout -b feature/yeni-ornek`)
3. Değişikliklerinizi Commit'leyin (`git commit -m 'Yeni örnek eklendi'`)
4. Dalınıza Push edin (`git push origin feature/yeni-ornek`)
5. Bir **Pull Request (PR)** açın

---

## ⭐ Destek Olun

Eğer bu repo Python öğrenme veya öğretme sürecinizde size yardımcı olduysa, lütfen bir **Yıldız (Star) ⭐** vererek projeyi öne çıkarın!

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında lisanslanmıştır. Dilediğiniz gibi kullanabilir, değiştirebilir ve paylaşabilirsiniz.
