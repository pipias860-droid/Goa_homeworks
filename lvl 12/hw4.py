price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
member = input("Are you a member? (yes/no): ")

if price >= 100 and quantity >= 3 and member == "yes":
    print("დიდი ფასდაკლება მიიღე")
    print("მადლობა ერთგული მომხმარებლობისთვის")

elif price >= 100 and quantity >= 3 and member == "no":
    print("ფასდაკლება მიიღო")
    print("წევრობის შემთხვევაში უფრო მეტს მიიღებ")

elif price < 50 or quantity == 1 or member == "no":
    print("ფასდაკლება არ გეკუთვნის")
    print("მეტი პროდუქტი შეიძინე")

else:
    print("მცირე ფასდაკლება მიიღე")
    print("გმადლობთ შენაძენისთვის")