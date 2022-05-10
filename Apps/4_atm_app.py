# ATM
ramazanHesap= {
    'ad':'Ramazan Erduran',
    'hesapNo' : '123123',
    'bakiye' : 1250,
    'ekHesap': 500,

}

aliHesap = {
    'ad':'Ali Veli',
    'hesapNo' : '321321',
    'bakiye' : 5000,
    'ekHesap': 2800,

}

def paraCek (hesap, miktar):
    print(f"Merhaba, {hesap['ad']}")
    if miktar <= hesap['bakiye']:
        hesap['bakiye'] -= miktar
        print(f"Para çekme işleminiz başarılı. Kalan bakiyeniz {hesap['bakiye']}")
    elif(miktar <= (hesap['bakiye']) + hesap['ekHesap']+1000):
        print("Bakiyeniz bu miktar için yetersiz.")
        fark = miktar - hesap['bakiye']
        print(f"{miktar} çekmek için ek hesabınızdan {fark} tl daha alınsın ister misiniz?")
        value = input("Yanıtınız (Evet / Hayır): ")
        value = value.lower()
        if value == 'hayır':
            print(f"Yanıtınızı {value} olarak kabul edip para çekme işleminizi iptal ediyoruz.")
        elif value == 'evet':
            if miktar <= (hesap['bakiye'] + hesap['ekHesap']):
                fark = miktar - hesap['bakiye']
                hesap['ekHesap'] -= fark
                hesap['bakiye'] = 0
                print("Para çekme işleminiz başarılı.")
                print(f"Yeni hesap bakiyeniz: 0 tl \nYeni Ek Hesap Bakiyeniz: {hesap['ekHesap']}")
            else:
                print("Ek hesabınıza baktık da, knk sen şu kartını al da git hadi yok o kadar paran...Ya Sabır!!")    
        else:
            print("Yanıtınızı dil bilimci bile anlayamaz ne diyonuz ??!!")
    else:
        print("O ek hesabını dahi devreye soksak sen o parayı çekemezsin. Lütfen sağdan yol al!!!")

paraCek(ramazanHesap,3500)
print("*"*50)