for i in range(200, 501):
    if i % 4 == 0 and i % 7 == 0:
        print(i)

    i = 200
while i <= 500:
    if i % 4 == 0 and i % 7 == 0:
        print(i)
    i += 1


#for:

for i in range(300, 1001):
    if i % 3 == 0 or i % 10 == 0:
        print(i)

    #while:

i = 300
while i <= 1000:
    if i % 3 == 0 or i % 10 == 0:
        print(i)
    i += 1


for i in range(1, 51):
    if i % 2 == 0:
        print("Even:", i)
    else:
        print("Odd:", i)


positive = 0
negative = 0

for i in range(10):
    num = int(input("Enter number: "))
    
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive:", positive)
print("Negative:", negative)


num = int(input("Enter number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Good")
elif num % 2 == 0:
    print("Two")
elif num % 3 == 0:
    print("Three")
else:
    print("None")


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



positive = 0
negative = 0

while True:
    num = int(input("Enter number (0 to stop): "))
    
    if num == 0:
        break
    elif num > 0:
        positive += 1
    else:
        negative += 1

print("Positive:", positive)
print("Negative:", negative)



num = int(input("Enter number: "))

for i in range(1, num + 1):
    if i % 4 != 0:
        print(i)


    for i in range(5):
    num = int(input("Enter number: "))
    
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")



    count = 0

while count < 5:
    num = int(input("Enter number: "))
    
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
    count += 1