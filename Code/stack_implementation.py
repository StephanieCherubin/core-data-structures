# https://leetcode.com/problems/valid-parentheses/

class Stack(s):
    # def __init__(self):
    #     self.items = []

    # def is_Empty(self):
    #     return self.items == []

    # def push(self):
    #     self.items.append(item)

    # def pop(self):
    #     return self.items.pop()
    
    # def peek(self):
    #     return self.items[len(self.items)-1]

    # def size(self):
    #     return len(self.items)
    
    left = ['(', '{', '[']
    right = [')', '}', ']']
    stack = []

    for character in s:
        if character in left:
            stack.append(character)
        elif character in right:
            if len(stack) <= 0:
                return False
            if left.index(stack.pop()) != right.index(character):
                return False
    return len(stack) == 0