x = 0
y= 0
while x < 10:
    x = x+1
    print(x)
    print("i'm in the loop")
    while y<5 :
        print(y)
        y = y+1
        print("inner loop")
        if y ==2:
          break
else :
    print("I'm out the loop")