class cons:
    def __init__(self):
        print("This is constructor method")
    def show(self):
        print("This is normal method")
    def __del__(self):
        print("This is Destructor method")
        print("object deleted")


ob=cons()
ob.show()
del ob