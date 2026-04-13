import numpy as np
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

totalMarks = np.sum(marks, axis=1)
avg_total = np.mean(totalMarks)
above_avg= totalMarks > avg_total
print("Total Marks:", totalMarks)
print("Class Average:", avg_total)
print("Above Average Students:", above_avg)