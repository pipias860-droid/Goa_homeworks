#input არის როცა შეგვყავს რაიმე ინფორმაცია საიტზე მაგალითად სახელი პაროლი და ასშ.



#output არის როცა მიღებულ ინფორმაცია ეკრანზე ან რამეზე გამოაქვს 



# პირველი მაგალითი სახელის ჩაწერა




name = input("enter your name: ")
print("Hello and wellcome", name)

#input იღებს საელს 
#print ბეჭდავს სახელს 

# მეორე მაგალითი სიტყვების შეერთება




number1= (input("enter your first word: "))

number2= (input("enter your second word: "))

combinedword = number1 + number2

print("and your word is...: ", combinedword)

#მესამე მაგალითი 


age = input("your age?: ")
print("you are", age, "years old")





#მეოთხე მაგალითი 

color = input("what is your fav color ?: ")
print("your fav color is..:", color)




#მეხუთე მაგალით 


n1= int(input("first number: "))
n2= int(input("second number: "))

answer = n1 + n2
print("answer is: ", answer)




name1= input("your name: ")

surname= input("your surname: ")

age1= input("your age?: ")

country= input("where are you from?: ")

print(name1 + " " + surname + " " + age1 + " " + country)