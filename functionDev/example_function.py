def first_example():
    global x
    x =20
    print(x)
    def first_example_test():
        x=50
        print(x)
    first_example_test()
def second_example():
    print(x)

first_example()
second_example()