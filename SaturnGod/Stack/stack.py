# stack.py
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
if __name__ == '__main__':
    stack = Stack()
    print(f"Is empty: {stack.is_empty()}")
    print(f"Push 4: {stack.push(7)}")
    print(f"Push dog: {stack.push('dog')}")
    print(f"Peek: {stack.peek()}")
    print(f"Push True: {stack.push(True)}")
    print(f"Size again: {stack.size()}")
    print(f"Push 8.4: {stack.push(8.4)}")
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")
    print(f"Size again: {stack.size()}")

    opens = "([{"
    closers = ")]}"
    print(opens.index("(")) # return 0
    print(opens.index("[")) # return 1
    print(closers.index("]")) # return 1
    print(closers.index("}")) # return 2
