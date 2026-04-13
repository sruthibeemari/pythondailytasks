import numpy as np
ratings = np.array([2, 3, 4, 5, 1])
normalized = (ratings - np.min(ratings)) / (np.max(ratings) - np.min(ratings))
print("Normalized Ratings:", normalized)