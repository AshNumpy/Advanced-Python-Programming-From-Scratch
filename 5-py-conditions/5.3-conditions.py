# Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet
# alabilme ya da alamama durumunu kontrol ediniz.

#Ehliyet için en az 18 ve üstü yaş lise veya üstü bir eğitim düzeyi olmalıdır.
"""
name= input("İsminiz:")
surname = input("Soyisminiz:")
age = int(input("Yaşınız:"))
edu = input("Eğitim durumunuz:")
edu = edu.lower()

if(age >= 18):
    if(edu == "lise" or edu == "üniversite" or edu == "lisans"):
        print("Ehliyet sınavına giriş hakkınız vardır.")
    else:
        print("Lisans durumunuzun yetersizliğinden ehliyet sınavına giremezsiniz.")
else:
    print("Yaşınızın yetersizliğinden dolayı ehliyet sınavına giremezsinzi.")
"""

# Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilerle
# göre hesaplayınız:

#   1. Bakım => 1. yıl 
#   2. Bakım => 2. yıl
#   3. Bakım => 3. yıl
#   ** süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayın.
#   *** datetime modülünü kullanmanız gerekiyor
#   (şimdi) - (2018/8/1) = gün

"""
days = int(input("Aracınız kaç gündür trafikte"))

if days <= 365:
    print("1. servis aralığı")
elif days > 365 and days <= 365*2:
    print("2. servis aralığı")
else:
    print("3. servis aralığı")
    """