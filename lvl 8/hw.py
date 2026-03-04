

str="sandro"
str2="nikora"
str3="nikoloz"
str4="giotgi"
str5="luka"

int=1
int=2
int=3
int=4
int=5

float=1.05
float2=2.05
float3=3.05
float4=4.05
float5=5.05

bool= True
bool2= False
bool3= 5 > 3
bool4= 10 >= 7
bool5= 1 < 2



#ოპერატორი არის ნიშანი ან სიმბოლო რომელიც გამოიყენება ცვლადებთან სამუშაოთ (მაგალითად +  - *  /  ==)

#ნასწავლი გვაქვს მარტო ლოგიკური და შედარებითი ოპერაციები 


print(8 > 17)
print(20 < 30)
print(6 >= 1)
print(154 <= 125)
print(99 >= 99)


age = 15

print(age > 10 and age < 18)  
print(age > 18 or age == 15)  
print(not(age > 18))          




num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))


if num1 > num2:
    print("1st number is bigger then the 2nd one")
else:
    print("1st number is not bigger then the 2nd one")






num1 = float(input("eneter 1st number: "))
num2 = float(input("enter 2nd number: "))


if num1 > 10:
    print("1st number is bigger then 10")
else:
    print("1st number is bigger then 10")


if num2 > 20:
    print("2nd number is bi8gger then 20")
else:
    print("2nd number is not bigger then 20")




num = int(input("Enter a number: "))

if 100 <= num <= 999:
    print("The number is between 100 and 999")
else:
    print("The number is not between 100 and 999")