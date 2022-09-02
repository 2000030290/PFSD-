try:
    klu1=open("file.txt","w")
    try:
        klu1.write("this is s1 section")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print("File opened successfully")
    klu1.close()
