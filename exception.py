try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a/b
    print("a/b=%d",c)
except Exception as e:
    print("cant divide by zero")
    print(e)
else:
    print("printing from else block")