while True:
    temp=input()
    with open('D:\Python\Projects\MajorProject\ChatImplementation\getpost\session.txt','w') as f:
        f.truncate(0)
        f.write(temp)
    with open('D:\Python\Projects\MajorProject\ChatImplementation\getpost\session.txt','r') as f:
        print(f.readlines())