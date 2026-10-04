# 4 basamaklı bir sayıyı yazıya çevirme 
def number_to_words(num):
    if not (1000 <= num <= 9999):
        return "Number must be a 4-digit integer."
    
    ones = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    tens = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    thousands = ["", "bin"]
    
    # Extract digits
    th = num // 1000
    h = (num % 1000) // 100
    t = (num % 100) // 10
    o = num % 10
    
    words = []
    
    if th > 0:
        words.append(ones[th])
        words.append(thousands[1])  # Add 'bin' for thousands place
    
    if h > 0:
        words.append(ones[h])
        words.append("yüz")  # Add 'yüz' for hundreds place
    
    if t > 0:
        words.append(tens[t])  # Add tens place
    
    if o > 0:
        words.append(ones[o])  # Add ones place
    
    return ' '.join(words).strip()
number_to_words(1234)  # Output: "bin iki yüz otuz dört"
print(number_to_words(1234))  # Output: "bin iki yüz otuz dört"

print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
#bir sayının pozitif tam bölenlerini bulan fonksiyon
def find_divisors(number):
    divisors = []
    for item in range (1, number + 1):
        if number % item == 0:
            divisors.append(item)
    return divisors
user_number = int(input("Bir sayi girin: "))
if user_number <= 0:
    print("Lütfen pozitif bir tam sayı girin.")
else:
    divisors = find_divisors(user_number)
    print(f"{user_number} sayısının pozitif tam bölenleri: {divisors}")
print("-------------------------------")
# yöntem 2 ileri seviye yaklaşım 
def find_divisors_advanced(number):
    divisors = [item for item in range(1, number + 1) if number % item == 0]
    return divisors

print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")

#pythonda banka hesap uygulaması ile ilgili örnek
def create_account(owner):
    return {"owner": owner, "balance": 0}
def desposit(account, amount):
    if amount > 0:
        account["balance"] += amount
        print(f"{amount} TL yatırıldı. Yeni bakiye: {account['balance']} TL")
    else:
        print("Lütfen pozitif bir miktar girin.")
def withdraw(account, amount):
    if 0 < amount <= account["balance"]:
        account["balance"] -= amount
        print(f"{amount} TL çekildi. Yeni bakiye: {account['balance']} TL")
    else:
        print("Yetersiz bakiye veya geçersiz miktar.")
def display_balance(account):
    print(f"{account['owner']} hesabının bakiyesi: {account['balance']} TL")
print("banka hesap uygulamasına hoş geldiniz!")
owner_name = input("Hesap sahibinin adını girin: ")
account = create_account(owner_name)
while True : 
    print("\nSeçenekler:")
    print("1. Para yatır")
    print("2. Para çek")
    print("3. Bakiye görüntüle")
    print("4. Çıkış")
    choice = input("Bir seçenek girin (1-4): ")
    
    if choice == "1":
        amount = float(input("Yatırmak istediğiniz miktarı girin: "))
        desposit(account, amount)
    elif choice == "2":
        amount = float(input("Çekmek istediğiniz miktarı girin: "))
        withdraw(account, amount)
    elif choice == "3":
        display_balance(account)
    elif choice == "4":
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")
