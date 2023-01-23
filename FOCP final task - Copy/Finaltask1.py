import random

names = ["Dhoni","Rohit","Virat","Ishan","Rishab","Kumar","Surya","Sikhar","Root",]
country = ["England","India","Australia","Pakistan","Lanka","Bangladesh","Afghanistan"]
ground = ["Lords","Oval","MCG","Wankhade","Chepauk","Chinnaswamy","SCG","Bowl"]

list = [n+c+g for n in names for c in country for g in ground]
print(len(set(list)))

print("Password generator is in progress!!!!!!")
print("*======================================*")
try:
    number = int(input("How many password is to be generated: "))
    if number < 1 or number > 24:
  # If the number is out of range, ask the user to enter a value between 1 and 24
        print("Please enter a value between 1 and 24.")
        exit()
    while True:
        if number == 0:
            print("Please enter a value between 1 to 24")
        for x in range(number):
            a = random.choices(names)+random.choices(country)+random.choices(ground)
            a=''.join(a)
            print(a)
            #print("Please enter atleast a digit")
        if number := 1:
            break
except ValueError:
    print("Please enter a number. ")   
print("Thank you")       