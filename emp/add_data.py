import csv
import random
import string

# Define the header row for the CSV file
header = ["EMP CODE", "EMP NAME", "BASIC SALARY", "DA", "GROSS SALARY", "NET SALARY", "IC", "PF", "TOTAL-DEDUCTIONS"]

# Define the list of possible values for each column
emp_codes = [f"EMP{str(i).zfill(4)}" for i in range(1, 1001)]
emp_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
min_basic_salary = 15000
max_basic_salary = 100000
da_percentage = 0.1
ic_percentage = 0.05
pf_percentage = 0.12

# Define the number of entries to generate
num_entries = 1000

# Generate the entries and write them to a CSV file
with open('employee_data.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(header)
    # Generate and write each entry
    for i in range(num_entries):
        emp_code = emp_codes[i]
        emp_name = random.choice(emp_names)
        basic_salary = round(random.uniform(min_basic_salary, max_basic_salary), 2)
        da = round(basic_salary * da_percentage, 2)
        gross_salary = round(basic_salary + da, 2)
        ic = round(gross_salary * ic_percentage, 2)
        pf = round(gross_salary * pf_percentage, 2)
        total_deductions = round(ic + pf, 2)
        net_salary = round(gross_salary - total_deductions, 2)
        row = [emp_code, emp_name, basic_salary, da, gross_salary, net_salary, ic, pf, total_deductions]
        writer.writerow(row)


