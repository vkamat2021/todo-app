files = ["a.txt", "b.txt","c.txt"]

for file in files:
    newFile = open(f"file1/{file}", 'r')
    content = newFile.read()
    print(content)
    newFile.close()
