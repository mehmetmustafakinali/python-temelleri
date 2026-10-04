#küçük büyük sesli sessiz harf uygulaması
my_char = input("Bir karakter girin: ")
if len(my_char) != 1 :
    print("Lütfen sadece bir karakter girin.")
else:
    if my_char.isalpha():
        if my_char.isupper():
            case = "büyük harf"
        else:
            case = "küçük harf"
            print(f"Girilen karakter {case}.")
        vowels = "aeiouAEIOU"
        if my_char in vowels:
            letter_type = "sesli harf"
        else:
            letter_type = "sessiz harf"
        print(f"Girilen karakter {letter_type}.")
    else:
        print("Girilen karakter bir harf değil.")
