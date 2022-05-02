print("****************\nGEOMETİK ŞEKİL HESAPLAMA PROGRAMINA HOŞGELDİNİZ\n****************")
seçim = input("LÜTFEN SEÇİM YAPINIZ ÜÇGEN VEYA DÖRTGEN:")

if (seçim == "ÜÇGEN"):
    print("lütfen kenar giriniz: ")
    a = int(input("1.kenar:"))
    b = int(input("2.kenar:"))
    c = int(input("3.kenar:"))
    if (a == b and b !=c ):
        print("ikizkenar üçgen")
    elif (a == c and b != c):
        print("ikizkenar üçgen")
    elif (b == c and c != a):
        print("ikizkenar üçgen")
    elif (a == b and b == c):
        print("eşkenar üçgen")
    elif (a + b < c):
        print("üçgen belirmiyor")
    elif (a + c < b):
        print("üçgen belirmiyor")
    elif (b + c < a):
        print("üçgen belirmiyor")
if( seçim == "DÖRTGEN"):
    q = int(input("1.kenarı giriniz :"))
    w = int(input("2.kenarı giriniz :"))
    e = int(input("3.kenarı giriniz :"))
    r = int(input("4.kenarı giriniz :"))
    if (q == w == e ==r):
        print("bu bir karedir")
    elif (q == w and e != r) :
        print("bu bir dikdörtgen")
    elif (q == e and w != r):
        print("bu bir dikdörtgen")
    elif (q == r and e != r) :
        print("bu bir dikdörtgen")
    else:
        print("sıradan bir dörtgen")



















