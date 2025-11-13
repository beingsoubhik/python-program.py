a = input("Enter text into the file:")
with open("output.txt", 'wt') as fs:
    fs.write(a+"\n")
    fs.close()
    print("Data successfully enter to 'output.txt'")

fh = open("output.txt", 'a')
fh.write ( input("Enter additional text to append:"))
fh.close()
print("Data successfully appended to 'output.txt'")

print("Final contents of 'output.txt':")
fh = open("output.txt", 'r')
with open ("output.txt", 'rt') as fz:
    print(fz.read())
