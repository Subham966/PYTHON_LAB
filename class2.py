class myfact:
    def fact(self,x):
        f=1
        for i in range(1,x+1):
            f=f*i
        print(f"Factorial value of {x} is {f}")

ob=myfact()
n=int(input("Enter a no to find factorial value: "))
ob.fact(n)