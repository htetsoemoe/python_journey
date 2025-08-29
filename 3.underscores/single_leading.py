class Test:
    def __init__(self):
        self._foo = 11
        self._bar = 12
        self.__baz = 12


class Extended_Test(Test): # Extend Test class
    def __init__(self):
        super().__init__()
        self._foo = "override"
        self._bar = "override"
        self.__baz = "override"


t = Test()
# print(dir(t))     
# print(t.__baz)

extended = Extended_Test()
print(dir(extended))
# print(extended.__baz)

print(f"Extended_Test__baz: {extended._Extended_Test__baz}")
print(f"Parent_Test__baz: {extended._Test__baz}")