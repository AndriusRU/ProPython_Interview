LIST_BRACKETS_1 = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '{([[}])'
]

LIST_BRACKETS_2 = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]

class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack or False

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def balance_stack(data):
    stack = Stack()
    for elem in data:
        if elem in "{[(":
            stack.push(elem)
        else:
            if stack.is_empty():
                return False
            elif stack.peek() + elem in ("()", "[]", "{}"):
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':

    list_brackets = LIST_BRACKETS_2
    for item in list_brackets:
        if balance_stack(item):
            print(f'Скобки "{item}" - сбалансированы')
        else:
            print(f'Скобки "{item}" - НЕ сбалансированы')

