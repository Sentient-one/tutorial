import numpy as np

arr1 = np.random.randint(0, 21, size=(3, 3))
arr2 = np.random.randint(0, 21, size=(3, 3))

print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)

addition = arr1 + arr2
print("\nMatrix Addition:")
print(addition)

multiplication = np.matmul(arr1, arr2)
print("\nMatrix Multiplication:")
print(multiplication)

transpose = multiplication.T
print("\nTranspose of Product Matrix:")
print(transpose)