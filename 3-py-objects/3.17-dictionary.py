
# key - value 
# 34 => İstanbul
# 41 => Kocaeli

sehirler = ["Kocaeli","İstanbul"] 
plakalar = [41,34]

print(plakalar[sehirler.index("İstanbul")])

# print(plakalar["Kocaeli"]) => 41 götürmeli 
# print(plakalar["İstanbul"]) => 34 götürmeli 

plakalar = {"Kocaeli" : 41 , "İstanbul":34 , "Konya":42}

print(plakalar["Konya"])

plakalar["Ankara"] = 6 #sözlüklere yeni veriler eklenebilir.
plakalar["Kocaeli"] = "New Value" #sözlükler güncellenebilir.

print(plakalar)


users = {
    "ramazanerduran":{
        "age":22,
        "roles" : ["user"],
        "mail": "ramazan.erduranq@outlook.com.tr",
        "adress":"beytepe yurdu",
        "phone": 123123123
    },
    "ramazanerduran2":{
        "age":222,
        "roles":["admin","user","moderatör"],
        "mail": "2ramazan.erduranq@outlook.com.tr",
        "adress":"2beytepe yurdu",
        "phone": 2123123123
    }
}

print(users["ramazanerduran"]["age"])
print(users["ramazanerduran2"]["roles"][0])
print(users["ramazanerduran2"]["roles"][:])

