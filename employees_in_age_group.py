#A program to display a histogram showing the number of employees in 
#specific age groups.

#emp _ages = [22,45,30,59, 58, 56,57,45,43,43,50,40,34,33,25,19]
#bins = [10,10,20,30,40,50,60]




import matplotlib.pyplot as plt

# Employee ages
emp_ages = [22, 45, 30, 59, 58, 56, 57, 45, 43, 43, 50, 40, 34, 33, 25, 19]

# Define the bins for the histogram
bins = [10, 20, 30, 40, 50, 60]

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(emp_ages, bins=bins, edgecolor='black', alpha=0.7)

# Adding titles and labels
plt.title('Histogram of Employee Ages')
plt.xlabel('Age Groups')
plt.ylabel('Number of Employees')

# Set the x-ticks to be the bin edges
plt.xticks(bins)

# Display the histogram
plt.grid(axis='y')  # Add grid lines for better readability
plt.show()