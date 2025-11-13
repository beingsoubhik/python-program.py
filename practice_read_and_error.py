try :
    with open("sample.txt", "rt") as file:
        data = file.read()
        print(data)
except FileNotFoundError :
     print(f"The file 'sample.txt' was not found. ")




