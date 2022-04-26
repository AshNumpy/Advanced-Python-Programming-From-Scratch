"""
    ogrenciler = {
        "120" : {
            "ad": "Ali",
            "soyad":"Yılmaz",
            "telefon":"123123123"
        },

        "125" : {
            "ad": "Ahmet",
            "soyad":"Narlı",
            "telefon":"123123123"
        },

        "128" : {
            "ad": "Ayşe",
            "soyad":"Kılıç",
            "telefon":"123123123"
        },
    }

    -Bilgileri verilen öğrencileri kullanıcıdan alınan bilgilerle dictionary içinde saklayınız.
    -Öğrenci numarasını kullanıcıdan alıp ilgili öğrencinin bilgilerini veriniz.

"""

ogrenciler = {}

number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci phone number: ")

ogrenciler.update({
    number: {
        "Adı" : name,
    "Soyadı" : surname,
    "Telefon no" : phone
    }
})


number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci phone number: ")

ogrenciler.update({
    number: {
        "Adı" : name,
    "Soyadı" : surname,
    "Telefon no" : phone
    }
})



number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci phone number: ")

ogrenciler.update({
    number: {
        "Adı" : name,
    "Soyadı" : surname,
    "Telefon no" : phone
    }
})



""" 2. Yöntem
ogrenciler[number] = {
    "Adı" : name,
    "Soyadı" : surname,
    "Telefon no" : phone,
}


number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci phone number: ")

ogrenciler[number] = {
    "Adı" : name,
    "Soyadı" : surname,
    "Telefon no" : phone,
}


number = input("Öğrenci no: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci phone number: ")

ogrenciler[number] = {
    "Adı" : name,
    "Soyadı" : surname,
    "Telefon no" : phone,
}
"""
print(ogrenciler)
print("*"*50)