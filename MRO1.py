class A:
    ...


class B(A):
    ...


class C(A):
    ...


class D(B, C):
    ...


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
help(D)