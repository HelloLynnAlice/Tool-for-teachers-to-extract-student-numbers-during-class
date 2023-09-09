import random
target=int(input("Please enter total number of prople:"))
while True:
    command=input("Press enter to generate,Press q to quit")
    if command=="q":
        break
    num1=random.randint(1,target+1)
    print(num1)
    num2=random.randint(1,target+1)
    while num1==num2:
        num2=random.randint(1,target+1)
    command=input("Press enter to generate,Press q to quit")    
    print(num2)    