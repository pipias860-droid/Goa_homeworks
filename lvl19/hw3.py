num = int(input("1st number: "))
max_num = num
min_num = num

for i in range(7):
    num = int(input("2nd number: "))
    
    if num > max_num:
        max_num = num
    
    if num < min_num:
        min_num = num

print("Maximux number is :", max_num)
print("Minimal number is :", min_num)