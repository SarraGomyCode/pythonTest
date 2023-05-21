example_demo = (1,2,8,85,9)
x = iter(example_demo)
print(next(x))
print(next(x))
y = sorted(example_demo)
print(y)
z = reversed(example_demo)
print(next(z))
w= sum(example_demo)
print(w)

def definition_value (x):
     print(int(x))
     print(int(x) + 20 )
definition_value(20)

def definition_name (name):
    print (f"Hello {name}")

definition_name ("sarra")


