sum_num = 0

while True:
    num = int(input("შეიყვანე რიცხვი: "))
    
    if num < 0:
        break
    
    sum_num += num

print("შეყვანილი რიცხვების ჯამია:", sum_num)