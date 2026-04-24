text = input("შეიყვანეთ ტექსტი: ")
n = len(text)

print(f"თქვენს ტექსტში" + " " + str(n)+" " + "სიმბოლოა")

# classwork2

numbers = [3, 7.5, 6, 6.5, 9, 14.5, 12, 19]

for i in range (len(numbers)):

    if numbers[i] % 3 == 0:
        print(numbers[i])