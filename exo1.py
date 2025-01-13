import numpy as np

# Matrice initiale
matrix = np.array([
    [12, 45, 78, 89],
    [56, 78, 90, 123],
    [34, 56, 78, 89],
    [45, 67, 89, 100],
    [23, 45, 67, 78],
    [78, 90, 123, 145],
    [56, 78, 90, 123],
    [34, 56, 78, 89]
])

# Min-Max Normalisation
X_min = np.min(matrix)   # Ou X_min = 0
X_max = np.max(matrix)   # Ou X_max = 255
normalized_matrix = (matrix - X_min) / (X_max - X_min)  # On utilise la première approche pour normaliser
print(normalized_matrix)