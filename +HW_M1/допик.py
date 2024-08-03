# a = {1, False, 0, True, None, 423}
# # print(a)
# # print(hash(1))
# # print(id(True))
# # print(id(1))
# # print(hash(True))
# print(hash(1) == hash(True))
# print(hash(1) is hash(True))
# print(id(1) is id(True))
# print(id(1) == id(True))
# print(hash(False))
# print(hash(0))
# print(hash(None))
# print(hash(423))


class CustomSet:
    def __init__(self):
        self.data = []

    def add(self, value):
        for item in self.data:
            if type(item) == type(value) and item == value:
                return
        print(value)
        self.data.append(value)

    def __contains__(self, value):
        for item in self.data:
            if type(item) == type(value) and item == value:
                return True
        return False

    def __repr__(self):
        elements = ', '.join(repr(item) for item in self.data)
        return f"{{{elements}}}"


a = CustomSet()
a.add(1)
a.add(True)
print(a)  # {1, True}
a.add(0)
a.add(False)
print(a)  # {0, 1, False, True}