def remember(cls):
    def inner(*args, **kwargs):
        print("I have been called")
        example = cls(*args, **kwargs)
        if args in example.children:
            example = example.children.pop(args)
        example.children[args] = example
        return example
    return inner


@remember
class A:
    children = {}

    def __init__(self, x, y=0, z=0):
        pass

    def __getitem__(self, item):
        item = item if isinstance(item, tuple) else (item, )
        return self.children[item]

    def __iter__(self):
        for key in self.children.keys():
            if len(key) == 1:
                key = key[0]
            yield key


a = A(1)
b = A(2, 3)
c = A(4, 5, 6)
d = A(1)
test = a[2, 3]
if test is b:
    print("Yey")

for i in d:
    print(i)

print(a[1] is a is d)

# Чтение файла с помощью итератора
#
# f = open("test.txt")
# for line in iter(lambda x: s.recv(1024), b""):
#   print(line)

from tempfile import NamedTemporaryFile, TemporaryFile
import time


with TemporaryFile("w+t") as f:
    f.writelines(["test", "asdasd", "asdasd"])
    time.sleep(3)

print("Destroyed")



# ==================================

class Node:

    def __init__(self, val):
        self._value = val
        self._children = {}
        # python

    def __repr__(self):
        return str(self._value)

    def add_children(self, *args):
        if len(set(args)) != len(args):
            print("Added only unique values")
        args = set(args)

        for item in args:
            self._children.update({item: Node(item)})

    def add_child(self, val):
        self._children.update({val: Node(val)})

    def remove_child(self, val):
        if val in self._children.keys():
            self._children.pop(val)

    def remove_all_children(self):
        self._children.clear()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def children(self):
        return self._children


gr = Node(1)
gr.add_children(2, 3, 4, 5)
gr.remove_child(5)
gr2 = Node(7)
gr2.add_children()
print(gr.children)


