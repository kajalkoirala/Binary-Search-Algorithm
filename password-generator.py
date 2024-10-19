import string 
import random

def generate_password(len=10):
    uppercase =  string.ascii_uppercase
    lowercase = string.ascii_lowercase
    number = string.digits
    char = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(number),
        random.choice(char)

    ]

    append_password = uppercase+lowercase+number+char
    password += [random.choice(append_password)for i in range(len -4)]

    random.shuffle(password)

    return "".join(password)

   

password = generate_password()
print(f"password: {password}")


while True:
    again = input("wanna generate again (Y?N)")
    if again.upper() == 'Y':
        password = generate_password()
        print(f"password: {password}")
        
    elif again.upper()=='N':
        print("thank you for beleving us")
        break

    else:
        print("enter the valid choice (Y/N)")



