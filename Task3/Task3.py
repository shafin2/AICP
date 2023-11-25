student_id= "23Y100012"
print(f"My strudent id is {student_id}")
slabs = [[55,65,75],[120,150,170],[210,230,240]]
def costSlab1():
    for i in range(3):
        print(slabs[0][i]*10,end=" ")
    print()
def costSlab2():
    for i in range(3):
        print(slabs[1][i]*15,end=" ")
    print()
def costSlab3():
    for i in range(3):
        print(slabs[2][i]*20,end=" ")
    print()
while True:
    print("Enter your choice")
    print("Press 1 to display the bill of slab 1 and slab 2")
    print("Press 2 to display the bill of slab 3")
    print("Press any other key to exist")
    user_input=int(input())
    if user_input==1:
        print("Bill for slab 1")
        costSlab1()
        print("Bill for slab 2")
        costSlab2()
        continue
    elif user_input==2:
        print("Bill for slab 3")
        costSlab3()
        continue
    else:
        break
