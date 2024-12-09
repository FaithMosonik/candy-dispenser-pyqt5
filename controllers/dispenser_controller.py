from models.stack import Stack
from models.candy import Candy

class DispenserController:
    def __init__(self):
        self.candy_stack = Stack()

    def push(self):
        try:
            candy = Candy()
            self.candy_stack.push(candy)
            return candy
        except Exception as e:
            return str(e)

    def pop(self):
        try:
            return self.candy_stack.pop()
        except Exception as e:
            return str(e)

    def peek(self):
        try:
            return self.candy_stack.peek()
        except Exception as e:
            return str(e)

    def get_candy_count(self):
        return self.candy_stack.size()

    def is_dispenser_empty(self):
        return self.candy_stack.is_empty()

    def is_dispenser_full(self):
        return self.candy_stack.is_full()