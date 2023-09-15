# Initialize an empty stack
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Peek at the top element
print("Peek:", stack[-1])  # Output: Peek: 3

# Pop elements from the stack
print("Pop:", stack.pop())  # Output: Pop: 3
print("Pop:", stack.pop())  # Output: Pop: 2

# Check if the stack is empty
print("Is stack empty?", len(stack) == 0)  # Output: Is stack empty? False

# Remaining stack
print("Stack:", stack)  # Output: Stack: [1]
