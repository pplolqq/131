
# tuple.__add__ = True
class A:
    def __init__(self,a) -> None:
        self.a = a
    def print(self):
        print("a")

    def pr():
        print("a")
class B(A):
    def __init__(self, a) -> None:
        super().__init__(a)
    def print(self):
        print("b")
class C(A):
    def __init__(self, a) -> None:
        super().__init__(a)
    def print(self):
        print("c")
def func(a:object):
    print(a(1).__ne__)
func(B)