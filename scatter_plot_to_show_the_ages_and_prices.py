
#A program to create a scatter plot to show the ages and prices of houses in Delhi

#age = [6,8,9,2,10,2,9,4,11,12,9]
#price = [97,87,82,120,77,122,99,97,74,79,83]

import matplotlib.pyplot as plt

# Data for ages and prices of houses
age = [6, 8, 9, 2, 10, 2, 9, 4, 11, 12, 9]
price = [97, 87, 82, 120, 77, 122, 99, 97, 74, 79, 83]

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(age, price, color='blue', marker='o')

# Adding titles and labels
plt.title('Scatter Plot of House Ages vs Prices in Delhi')
plt.xlabel('Age of House (Years)')
plt.ylabel('Price of House (in Lakhs)')

# Displaying the scatter plot
plt.grid(True)  # Add grid lines for better readability
plt.show()

