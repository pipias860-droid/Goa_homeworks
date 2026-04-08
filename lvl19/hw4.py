n= int(input("your number:"))
count=0

for i in range (1, n + 1):
    if i % 3 == 0:
        count += 1 

    print("3-ზე იყოფა:", count)