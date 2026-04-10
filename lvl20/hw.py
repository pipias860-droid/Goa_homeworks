colors = ["red","purple","blue"]

days = ["ორშაბათი","სამშაბათი","ოთხშაბათი","ხუთშაბათი","პარასკევი","შაბათი","კვირა"]





numbers = [1 , 2 , 5 , 7 , 3 ]

print(numbers[3])

cities = ["თბილისი","რუსთავი","ბათუმი","გორი","ქუთაისი"]

cities[2] = "ზუგდიდი"

print(cities)


family = ["დედა", "ბებია" , "მამა"]

print(family[0])

print(family[2])




numbers = [5, 12, 7, 20, 33, 9]

numbers[4] = 100

print(numbers)





dogs = ["რექსი", "ბუბა", "ლუნა", "მაქსი", "ჩაპი", "კოკო", "ლეო", "ჯესი", "ტობი", "ბრუნო"]

dogs[4] = "სნუპი"

print(dogs)




data = ["მე", "მიყვარს", "python", 16, 68, 57, True, False, True]

print(data[2])  



musicians = ["Drake", "Eminem", "Travis Scott", "Kanye West", "50 Cent"]

if musicians[0] == "Drake":
    musicians[0] = "The Weeknd"

print(musicians)



numbers = [10, 5.5, 20, 7.2, 3]

numbers[0] += 1000
numbers[-1] += 1000

print(numbers)



nums = [12, 3.5, 2]

if nums[0] > 10:
    nums[2] += nums[0] * nums[1]
else:
    nums[0] += nums[1] * nums[2]

print(nums)