#A program to display a pie chart showing the percentage of expenditures in each
#department of a company.

#take the expenditures of 4 departments
#slices = [50, 14, 24, 16]

#take the departments names
#depts = ['Sales', 'Production', 'HR', 'Finance"]

#take the colors for each department
#cols = ['magenta', 'cyan', 'brown', 'gold"]



import matplotlib.pyplot as plt

# Expenditures of 4 departments
slices = [50, 14, 24, 16]

# Department names
depts = ['Sales', 'Production', 'HR', 'Finance']

# Colors for each department
cols = ['magenta', 'cyan', 'brown', 'gold']

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(slices, labels=depts, colors=cols, autopct='%1.1f%%', startangle=140)

# Adding a title
plt.title('Percentage of Expenditures in Each Department')

# Display the pie chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
