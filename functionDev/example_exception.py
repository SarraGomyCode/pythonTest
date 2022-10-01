try:
    print("input please to mention x :  " )
    x = int(input())
    print("input please to mention y :  " )
    y= int(input())
    if y == 0:
        raise Exception ("it's a new exception ")
    print(x/y)
except Exception as e:
    print(e)
    print("first exception")
else:
    print("it's else block")
finally:
    print("always to be executed")