import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
studie_uren = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
oefentoetsen = np.array([2, 3, 3, 4, 5]).reshape(-1, 1)
motivatie = np.array([3, 5, 7, 8, 9]).reshape(-1, 1)  # Motivatie toegevoegd
cijfers = np.array([3, 4.5, 5, 6.5, 8])

# Combineer de drie variabelen in een matrix
X = np.hstack((studie_uren, oefentoetsen, motivatie))

# Display X
print(X)

# Model aanmaken en trainen
model = LinearRegression()
model.fit(X, cijfers)

# Voorspellingen maken
predictions = model.predict(X)

# Coëfficiënten en intercept
print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")  # b1, b2, en b3

# Voorspellingen weergeven
print(f"Voorspelde cijfers: {predictions}")

# Plotten van voorspellingen en werkelijke gegevens
fig, ax = plt.subplots()
ax.scatter(range(len(cijfers)), cijfers, color='blue', label='Werkelijke cijfers')
ax.plot(range(len(cijfers)), predictions, color='red', label='Voorspelde cijfers')
plt.xlabel('Studenten (volgorde)')
plt.ylabel('Cijfers')
plt.legend()
plt.show()
