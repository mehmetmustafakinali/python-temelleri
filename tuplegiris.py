# ==========================================
# Python Demetler (Tuples) - Kapsamlı Rehber
# ==========================================

# 1. Tuple Tanımlama
# Demetler (tuple), sıralı (ordered) ve DEĞİŞTİRİLEMEZ (immutable) veri yapılarıdır.
# Parantez () kullanılarak oluşturulur.

demet = ("elma", "armut", "muz", "çilek")
print("Demet:", demet)
print("Veri Tipi:", type(demet))
print("Eleman Sayısı:", len(demet))

# Tek elemanlı tuple oluştururken sonuna MUTLAKA virgül konulmalıdır:
tek_elemanli = ("elma",)
print("Tek elemanlı tip:", type(tek_elemanli))  # <class 'tuple'>

yaniltici = ("elma")
print("Virgülsüz tanımlama:", type(yaniltici))  # <class 'str'>

# Farklı veri tiplerini bir arada tutabilir:
karisik = ("Ahmet", 25, 3.14, True, [1, 2, 3])
print("Farklı veri tipleri:", karisik)

# ------------------------------------------
# 2. İndeksleme ve Dilimleme (Indexing & Slicing)
# ------------------------------------------
sayilar = (10, 20, 30, 40, 50, 60)

print("İlk eleman (sayilar[0]):", sayilar[0])
print("Son eleman (sayilar[-1]):", sayilar[-1])
print("Belirli aralık (sayilar[1:4]):", sayilar[1:4])
print("Ters çevirme (sayilar[::-1]):", sayilar[::-1])

# ------------------------------------------
# 3. İmmutability (Değiştirilemezlik) İlkesi
# ------------------------------------------
# demet[0] = "karpuz" -> TypeError: 'tuple' object does not support item assignment
# Tuple doğrudan değiştirilemez, ancak listeye dönüştürülüp düzenlenebilir:

meyve_listesi = list(demet)
meyve_listesi.append("karpuz")
yeni_demet = tuple(meyve_listesi)
print("Dönüşüm sonrası güncellenen demet:", yeni_demet)

# ------------------------------------------
# 4. Tuple Metotları (count, index)
# ------------------------------------------
rakamlar = (1, 2, 3, 2, 4, 2, 5)

# count(): Belirtilen elemanın kaç kez geçtiğini sayar
kac_tane = rakamlar.count(2)
print("2 rakamı kaç defa var:", kac_tane)

# index(): Belirtilen elemanın ilk bulunduğu indeks numarasını verir
indeks = rakamlar.index(4)
print("4 sayısının indeksi:", indeks)

# ------------------------------------------
# 5. Tuple Paketleme & Çözme (Unpacking)
# ------------------------------------------
kisi = ("Mehmet", 24, "Yazılım Geliştirici")
isim, yas, meslek = kisi
print(f"İsim: {isim}, Yaş: {yas}, Meslek: {meslek}")

# Genişletilmiş Çözme (*args mantığı):
sayi_grubu = (1, 2, 3, 4, 5, 6)
ilk, *orta, son = sayi_grubu
print("İlk:", ilk)
print("Orta elemanlar (liste):", orta)
print("Son:", son)

# ------------------------------------------
# 6. Tuple Avantajları
# ------------------------------------------
# 1. Hızlıdır (Listelere göre bellekte daha az yer kaplar ve erişimi daha hızlıdır).
# 2. Güvenlidir (Değiştirilemez olduğu için verinin kazara değiştirilmesini önler).
# 3. Sözlüklerde (dict) anahtar (key) olarak kullanılabilir.
sozluk = {
    (41.0082, 28.9784): "İstanbul",
    (39.9334, 32.8597): "Ankara"
}
print("Koordinat Sözlüğü:", sozluk[(41.0082, 28.9784)])
