print("Enter name : ",end='')
name = input()
print("Enter SAP-ID : ",end='')
sapid = input()
print("Enter Date Of Birth : ",end='')
dob = input()
print("Enter Address : ",end='')
add = input()
print("Enter Program : ",end='')
prog = input()
print("Enter semester number : ",end='')
sem = input()
print("NAME : ", name.upper())
print("SAP ID : ", sapid)
print("DATE OF BIRTH : ", dob)
x = "ADDRESS : "
print(x,end='')
l = add.split(" ")
i = 0
for i in range(len(l)):
    print(l[i])
    print(' '*len(x),end='')
print()
print("PROGRAM : ",prog)
print("SEMESTER : ",sem)