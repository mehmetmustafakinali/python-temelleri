#random module
import random
random.seed(42)  # seed değeri 42 olarak ayarlanır

print(random.random())
#random  da seed ne demek? random modülünde seed, rastgele  sayı üreteci için başlangıç değerini belirler. Seed değeri aynı olduğunda, random modülü aynı rastgele sayı dizisini üretir. Bu, testler ve tekrar üretilebilir sonuçlar için faydalıdır.
#getstate() fonksiyonu, random modülünün mevcut durumunu döndürür. Bu durum, rastgele sayı üreteci için kullanılan dahili durumu temsil eder. Bu durumu kaydedebilir ve daha sonra aynı durumu geri yükleyerek aynı rastgele sayı dizisini yeniden oluşturabilirsiniz.
state = random.getstate()
print(state)
#setstate() fonksiyonu, random modülünün durumunu ayarlamak için kullanılır. Bu, daha önce kaydedilmiş bir durumu geri yüklemek için kullanılabilir. Bu sayede aynı rastgele sayı dizisini yeniden oluşturabilirsiniz.
random.setstate(state)
#getrandbits() fonksiyonu, belirli bir bit sayısına sahip rastgele bir tamsayı döndürür. Örneğin, random.getrandbits(8) 0 ile 255 arasında rastgele bir tamsayı döndürür.
rand_bits = random.getrandbits(8)                   
#randrange() fonksiyonu, belirli bir aralıkta rastgele bir tamsayı döndürür. Örneğin, random.randrange(1, 10) 1 ile 9 arasında rastgele bir tamsayı döndürür.
rand_range = random.randrange(1, 10)
print(rand_bits)
print(rand_range)
print("----------------------------------------------------------------" \
"")
rand_range= random.randrange(1, 10, 2)  # 1 ile 9 arasında rastgele bir tek sayı döndürür
print(rand_range)

print("----------------------------------------------------------------" \
"")
print(random.choice(["apple", "banana", "cherry"]))  # listeden rastgele bir öğe seçer,ü
print(random.choice("Hello World"))  # stringden rastgele bir karakter seçer
print("----------------------------------------------------------------" \
"")
#choices ise rastgele seçim yapar ve seçilen öğeleri bir liste olarak döndürür. Örneğin, random.choices(["apple", "banana", "cherry"], k=2) 2 rastgele öğe seçer ve bir liste olarak döndürür.
print(random.choices(["apple", "banana", "cherry"], k=2)) 
#shuffle ise bir listeyi karıştırır ve orijinal listeyi değiştirir. Örneğin, random.shuffle(mylist) mylist listesini karıştırır.
mylist = [1, 2, 3, 4, 5]
random.shuffle(mylist)
print(mylist)
print("----------------------------------------------------------------" \
"") 
#sample ise bir popülasyondan rastgele örnekler seçer ve seçilen örnekleri bir liste olarak döndürür. Örneğin, random.sample([1, 2, 3, 4, 5], k=3) 3 rastgele öğe seçer ve bir liste olarak döndürür.
print(random.sample([1, 2, 3, 4, 5], k=3))
#choice ile farkı, choice tek bir öğe seçerken, sample birden fazla öğe seçebilir ve seçilen öğeleri bir liste olarak döndürür.
#choices ile farkı, choices seçilen öğeleri bir liste olarak döndürürken, sample seçilen öğeleri bir liste olarak döndürür ve aynı öğe birden fazla kez seçilemez.         
print("----------------------------------------------------------------" \
"")
#üniform da rastgele sayı üretir. Örneğin, random.uniform(1, 10) 1 ile 10 arasında rastgele bir float döndürür.
rand_uniform = random.uniform(1, 10)
print(rand_uniform)  
print("----------------------------------------------------------------" \
"")
#triangular da rastgele sayı üretir. Örneğin, random.triangular(1, 10, 5) 1 ile 10 arasında rastgele bir float döndürür ve 5'e yakın olma olasılığı daha yüksektir.
rand_triangular = random.triangular(1, 10, 5)
print(rand_triangular)