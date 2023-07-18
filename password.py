import random
import sys
import string


option=int(sys.argv[1])
length=int(sys.argv[2])
#print(option)
#print(length)
#print(string.digits)
#print(string.punctuation)
generate=''
if option==1:

    pass_combined = string.ascii_letters
    for i in range(length):
        temp=random.choice(pass_combined)
        generate=generate+temp
    print("Password : ",generate)   
elif option==2:
    pass_combined = string.ascii_letters + string.digits
    for i in range(length):
        temp=random.choice(pass_combined)
        generate=generate+temp
    print("Password : ",generate) 

elif option==3:
    pass_combined = string.punctuation + string.ascii_letters 
    for i in range(length):
        temp=random.choice(pass_combined)
        generate=generate+temp
    print("Password : ",generate)  
elif option==4:
    pass_combined = string.punctuation + string.ascii_letters + string.digits
    for i in range(length):
        temp=random.choice(pass_combined)
        generate=generate+temp
    print("Password : ",generate)  
else:
    print("Invalid option")

