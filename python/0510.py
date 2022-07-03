class A:
    first = 1
    def __init__(self):
        self.second = 2
aa = A()
bb = A()

bb.first = 11
print(id(bb.first))
print(id(A.first))
A.first = 10
print(id(bb.first))
print(id(A.first))