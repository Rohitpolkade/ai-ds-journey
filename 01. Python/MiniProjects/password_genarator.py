# Random PassWord Generator !!
import random
import string
'''it is a inbuilt module || which carry all
 upper case,lower case,digits,punctuators'''

charValues =string.ascii_letters +string.digits + string.punctuation
pass_len=12
'''password=""
for i in range(pass_len):
    password+=random.choice(charValues)

print("your random password is :",password)'''

#By list Comprehension [function for i in range(n)]

password= "".join([random.choice(charValues) for i in range(pass_len)])
print("your password is :",password)