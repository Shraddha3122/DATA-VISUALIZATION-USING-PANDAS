# A program to display employee id numbers on X-axis and their salaries on Y-axis in
#the form of a bar graph for two departments of a company.

#take employee ids and salaries for sales dept
#x = [1001, 1003, 1006, 1007, 1009. 1011]
#y= [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99]

#take employee ids and salaries for Production dept
#x1= [1002, 1004, 1010, 1008, 1014, 1015]
#y1= [5000, 6000, 4500.00, 12000, 9000, 10000]




import matplotlib.pyplot as plt
import numpy as np

# Employee IDs and salaries for Sales department
sales_ids = [1001, 1003, 1006, 1007, 1009, 1011]
sales_salaries = [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99]

# Employee IDs and salaries for Production department
production_ids = [1002, 1004, 1010, 1008, 1014, 1015]
production_salaries = [5000, 6000, 4500.00, 12000, 9000, 10000]

# Combine the data for plotting
all_ids = sales_ids + production_ids
all_salaries = sales_salaries + production_salaries

# Create an array for the X-axis positions
x_positions = np.arange(len(all_ids))

# Create the bar graph
plt.figure(figsize=(12, 6))
plt.bar(x_positions[:len(sales_ids)], sales_salaries, color='skyblue', label='Sales Dept', width=0.4, align='center')
plt.bar(x_positions[len(sales_ids):], production_salaries, color='lightgreen', label='Production Dept', width=0.4, align='edge')

# Adding titles and labels
plt.title('Employee Salaries by Department')
plt.xlabel('Employee ID')
plt.ylabel('Salary')
plt.xticks(x_positions, all_ids)  # Set x-ticks to be the employee IDs
plt.legend()  # Show legend

# Displaying the bar graph
plt.grid(axis='y')  # Add grid lines for better readability
plt.show()