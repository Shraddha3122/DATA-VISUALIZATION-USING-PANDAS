#A Python program to display employee id numbers on X-axis and
#their salaries on Y-
#axis in the form a bar graph.

#empdata = { "empid": [1001, 1002, 1003, 1004, 1005, 1006],
 #                    "ename": ["Ganesh Rao", "Anil Kumar", "Gaurav Gupta", "Hema Chandra", "Laxmi Prasanna", "Anant Nag"].
  #                   "sal": (10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999,99),
   #                 "doj": ["10-10-2000", "3-20-2002", "3-3-2002", "9-10-2000", "10-8-2000","9-9-1999"] }



import matplotlib.pyplot as plt

# Employee data
empdata = {
    "empid": [1001, 1002, 1003, 1004, 1005, 1006],
    "ename": ["Ganesh Rao", "Anil Kumar", "Gaurav Gupta", "Hema Chandra", "Laxmi Prasanna", "Anant Nag"],
    "sal": [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99],
    "doj": ["10-10-2000", "3-20-2002", "3-3-2002", "9-10-2000", "10-8-2000", "9-9-1999"]
}

# Extracting employee IDs and salaries
emp_ids = empdata["empid"]
salaries = empdata["sal"]

# Creating the bar graph
plt.figure(figsize=(10, 6))
plt.bar(emp_ids, salaries, color='skyblue')

# Adding titles and labels
plt.title('Employee Salaries')
plt.xlabel('Employee ID')
plt.ylabel('Salary')

# Displaying the bar graph
plt.xticks(emp_ids)  
plt.grid(axis='y')  
plt.show()



