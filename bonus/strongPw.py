password = input("Enter your password: ")
result = {}
if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

char = False
for i in password:
    if i.isupper():
        char = True

result["Uppercase"] = char

print(result)
print(result.values())

if all(result.values()):
    print("Password is Strong")
else:
    print("Input a stronger password")


