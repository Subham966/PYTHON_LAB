class A:
    pass

class B:
    pass

class C:
    pass

class D(A,B,C):
    pass

class E(B,C):
    pass

class F(D,E):
    pass

print(F.mro())          # MRO = Method Resolution Order
