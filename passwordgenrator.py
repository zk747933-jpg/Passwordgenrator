import string
import secrets
password_length = int(input("enter the length of your password"))

all_characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(secrets.choice(all_characters) for i in range(password_length))

print("your secure password is",password)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#2nd method 
import string 
import secrets


password_length = int(input("enter the length of your password"))
all_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(all_characters) for i in range (password_length))
print("yur secure password  is",password)