
temp= int(input("რა არის თქვენი ტემპერატურა?: "))

if temp >= 0:
    print("ცივა")
if temp >= 10:
    print("ცოტა ცივა ")
if temp >= 20:
    print("სასიამოვნო ამინდია ")
if temp >= 30:
    print("ძალიან ცხელა")
if temp <= -0:
    print("საშინლად ცივა სახლში დარჩი")



score= int(input("შეიყვანე შენი ქულა: "))

attendance= int(input("შეიყვანე შენი დასწრება (%): "))

if score > 80 and attendance > 90:
    print("შენ შესანიშნავად დაწერე გამოცდა")
elif score > 50 and attendance > 70:
    print("საშუალოდ დაწერე გამოცდა")
elif score > 30 and attendance > 50:
    print("გაჭირვებით, მაგრამ ჩააბარე გამოცდა")
else:
    print("ჩაიჭერი")



temp1= input("რა ტემპერატურაა თქვენთნ?: ")

rain= bool(input("არის თქვენთან წვიმა?(no/yes) "))

if temp > 25 and rain =="no":
    print("შესანიშნავი ამინდია სასეირნოდ!")
elif temp > 25 and rain == "yes":
    print("ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!")

elif temp < 10 or rain == "yes":
    print("სჯობს სახლში დარჩე")

else:
    print("სასიამოვნო ამინდია")


age= int(input("რა არის შენი ასაკი?: "))
student=input("სტუდენტი ხარ?(yes/no)")

if age < 12 or age > 65:
    print("ბილეთი უფასოა")
elif student == "yes" and age > 12:
    print("ბილეთი ნახევარ ფასად")
elif student=="no"  and age < 12:
    print("სრული ფასი უნდა გადაიხადო")

username=input("what is your user?: ")
password=int(input("password?: "))

if username=="guest" and password=="1234":
     print("მოგესალმები, სტუმარო!")
elif username=="admin" and password=="superSecretPassword":
     print("მოგესალმები, ადმინ!")
else:
    print("მომხმარებელი არ მოიძებნა!")