# Stack :- 
# stack = []

# add elements 
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# print("The original List =",stack)
# o/p = The original List = [10, 20, 30, 40]
# remove element 
# stack.pop()
# print("The Updated List after pop =",stack)
# o/p = The Updated List after pop = [10, 20, 30]

# peek operation 
# print("Top element is =",stack[-1])
# Top element is = 40
# task: check if stack is empty or not.

# ----------------Queue---------------------------- 
from collections import deque 

operation = deque() 

# Add elements 
operation.append(20)
operation.append(40)
operation.append(60)
operation.append(10)
operation.append(30)
print("original Queue=",operation)
# o/p =original Queue= deque([20, 40, 60, 10, 30])
print("Removed left element is=",operation.popleft())
# o/p =Removed left element is= 20 

# task =queue is empty or not ?


