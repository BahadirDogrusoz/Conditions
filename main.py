number = 30

if number > 10:
    print("Sayı 10'dan büyük")

else:
    print("Sayı 10 veya 10'dan küçüktür")

print("-------------------------------------------------")

weather = "Güneşli"

if weather == "Yağmurlu":
    print("Hava yağmurlu")

elif weather == "Güneşli":
    print("Hava güneşlidir")

elif weather == "Karlı":
    print("Hava karlıdır")

else:
    print("Hava bulutludur")

print("-------------------------------------------------")

username = input("Kullanıcı adınızı giriniz: ")
password = input("Şifrenizi giriniz: ")

if username == "boncuk" and password == "12345678":
    print("Sisteme başarıyla giriş yaptınız! Tebrikler")

else:
    print("Kullanıcı adı veya şifre yanlış")

print("-------------------------------------------------")

number2 = int(input("Bir sayı giriniz: "))

if number2 % 2 == 0 or number2 % 3 == 0:
    print("Sayı ikiye ve üçe veya ikisinden birisine bölünebiliyor!")

else:
    print("Sayı ne ikiye ne de üçe bölünemiyor!")

