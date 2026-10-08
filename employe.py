import csv
import sys
if len(sys.argv) < 2:
    print("Please provide the CSV filename.")
    sys.exit()

filename = sys.argv[1]
if len(sys.argv) < 2:
    print("Please provide the CSV filename.")
    sys.exit()

filename = sys.argv[1]

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

    print("\n--- Employee Records ---")

for employee in employees:
    print(employee)
emp_id = input("\nEnter Employee ID to search: ")

found = False

for employee in employees:
    if employee["Employee ID"] == emp_id:
        print("\nEmployee Found:")

        for key, value in employee.items():
            print(key, ":", value)

        found = True
        break
    if not found:
        print("Employee not found.")