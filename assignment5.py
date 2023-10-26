import random
pc_num=random.randint(0,10)
n=0
while True:
    user_num=int(input("Enter num: "))
    n+=1
    if user_num==pc_num:
        print("correct")
        break
    if user_num<pc_num:
        print("enter biger number plz")
    if  user_num>pc_num:
        print("enter smaller number")    
print("How many times have you guessed?",n)        

