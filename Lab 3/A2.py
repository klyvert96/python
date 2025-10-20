import string

password = input()

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-#*"

if all(symbol in allowed for symbol in password) and \
   len(password) == 8 and \
   password.lower() != password and \
   password.upper() != password and \
   any(symbol.isdigit() for symbol in password) and \
   any(symbol in "-#*" for symbol in password):
    print("Strong password")
else:
    if len(password) != 8:
        print("Password length is not 8")
    if password.lower() == password:
        print("No uppercase letters")
    if password.upper() == password:
        print("No lowercase letters")
    if not any(symbol.isdigit() for symbol in password):
        print("No digits")
    if not any(symbol in "-#*" for symbol in password):
        print("No special characters")
    if not all(symbol in allowed for symbol in password):
        print("Contains invalid characters")
