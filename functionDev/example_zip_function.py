list1 = [1,2,89,50]
list2 = [94,97,20,30]

s = zip(list1,list2)
print(list(s))

for x,y in zip(list1,list2):
   print(x-y)