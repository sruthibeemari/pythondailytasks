import numpy as np
nums = np.random.randint(1, 100, 10)
filtered = nums[nums % 5 == 0]
sorted = np.sort(filtered)
print("Random Numbers:", nums)
print("Filtered (divisible by 5):", sorted)