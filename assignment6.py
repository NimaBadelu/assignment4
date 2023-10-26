import random
print("b")
while True:
    order=input("dice or end:")
    if order=="end":
        print("d")
        break
    if  order=="dice":
        pc_num=random.randint(1,6)
        print(pc_num)
    if pc_num==6:
        order=input("dice or end: ")
        if order=="end":
            break
        if order=="dice":
               for i in range (2):
                    pc_num=random.randint(1,6)
                    print(pc_num)
            