import numpy as np

left = np.random.randint(1, 40, size= 1)
right = np.random.randint(1, 50, size = 1)
students = np.column_stack((left, right))

print("All score list")
print(students)

midterm = students[students[:, 0]>=25]
result = midterm[midterm[:, 1]>=30]

print(result)