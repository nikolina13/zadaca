Raspolozenje = input("Kako se osjecas: ")
if Raspolozenje == "sretno":
    print("Super")
elif Raspolozenje == "tužno":
    print("Bed")
elif Raspolozenje == "nervozno":
    print("Diši duboko")
elif Raspolozenje == "uzbuđeno":
    print("Ayyyyy")
elif Raspolozenje == "opušteno":
    print("Samo lagano")
else:
    print("Ne znam kako ti je")

secret=int(13)
guess=int(input("Pogodi broj do 20"))
if secret==guess:
    print("Bravo, pogodak!")
else:
    print("Promašaj")


a = int(input("unesi prvi broj za računanje"))
b = int(input("unesi drugi broj za računanje"))
operacija = input("Unesi matematičku operaciju (+,-, ili /)")
if operacija == "+" :
    print(a + b)
elif operacija == "-" :
    print(a - b)
elif operacija == "*" :
    print(a * b)
elif operacija == "/" :
    print(a / b)
else:
    print("krivo unešeni podaci")