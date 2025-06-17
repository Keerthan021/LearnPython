with open("file.txt","r") as rfile:
    content = rfile.read()
    print(content)

with open('file.txt', 'w') as wfile:
    wfile.write("This is first line\n")
    wfile.write("This is second line\n")
    wfile.write("This is third line\n")

with open("file.txt","r") as rfile:
    content = rfile.read()
    print(content)

