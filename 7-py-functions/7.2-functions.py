# Functions

# def function_name():
#     actions

def sayHello(name = "user"):
    print("Hello " + name)

sayHello()
sayHello("ramazan")

#****************************
def sayHello(name = "user"):
    return "Hello " + name

msg = sayHello("Ramazan")
print(msg)

#****************************
def total(num1, num2):
    return num1 + num2

print(total(10,20))

#****************************
def emeklilik(dogumYili, prim):
    def yasHesapla(dogumYili):
        return 2022 - dogumYili
    a = yasHesapla(dogumYili)
    emeklilik = 55 - a
    primGunu = 50 - prim
    if emeklilik <= 0:
        if primGunu <= 0:
            print("Emekli olma şartlarını sağlıyorsunuz.")
        else:
            print(f"Emeklilik yaşınız yeterli fakat emeklilik için daha {primGunu} priminiz var.")
    elif primGunu <= 0:
        if emeklilik > 0:
            print(f"Priminiz dolmuş fakat emekli olmak için daha {emeklilik} yılınız var")
    else:
        print(f"Emekli olmak için daha {emeklilik} yılınız ve dolması gereken {primGunu} priminiz var.")

a = int(input("Doğum yılınız: "))
b= int(input("Dolmuş prim gününüz: "))
emeklilik(a,b)

#*******************************
print(help(emeklilik))