# 1. Allow users to choose to register or login
#If register
# 2. Enter username and password.
# 3. Validate password for length, capitals and not just letters.
# 4. Make them input a message to store
# 5. Once registered add object to text file with username, password and message
#If login
# 6. If login find object with username the same
# 7. Check if password is the same if so, display message
import bcrypt
def isLongerThan8(password):
    if(len(password)>=8):
        return True
    else:
        return False
def capitalsAndLowerCase(password):
    if(password!=password.lower() and password!=password.upper):
        return True
    else:
        return False
def includesNumbers (password):
    return any(character.isdigit() for character in password)

def register():
    username=input("Choose your username:\n")
    while True:
        password=input("Choose your password:\n")
        if(not isLongerThan8(password)):
            print("Your password needs to be longer than 8 characters.")
        elif(not capitalsAndLowerCase(password)):
            print("Your password needs to have upper and lower case.")
        elif(not includesNumbers(password)):
            print("Your password needs to have numbers.")
        else:
            break
    message=input("Input your message you want to save: ")
    password=password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashedPassword=bcrypt.hashpw(password,salt)
    user={
        "username":username,
        "password":hashedPassword,
        "message":message
        }
    f=open("users.txt","a")
    f.write(str(user)+"\n")
    f.close()
def login():
    username=input("Enter your username:\n")
    password=input("Enter your password:\n")
    password=password.encode("utf-8")
    f=open("users.txt","r")
    users=f.readlines()
##    for line in f:
##        users.append(line)
    f.close()
    users=list(map(lambda x:eval(x.strip()),users))
    for user in users:
        if(user.get("username")==username):
            if bcrypt.checkpw(password,user.get("password")):
                print("Logged In")
                print("Your message is:\n"+user.get("message"))
registerOrLogin=input("Do you want register or login? (register/login)\n")
if(registerOrLogin=="register"):
    register()
else:
    login()
    
