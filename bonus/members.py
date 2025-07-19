file = open('../files/members.txt', 'r')
content = file.read()
file.close()
# print(content)
newMem = "\n" + input("Enter new member:")
newContent = content + newMem
newFile = open('../files/members.txt', 'w')
newFile.write(newContent)
newFile.close()
