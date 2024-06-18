import csv
from faker import Faker

fake = Faker()

num_records = 30
data = []
for _ in range(num_records):
    name = fake.name()
    roll_number = fake.random_int(min=1000, max=9999)
    roll_number = f"21311A{roll_number}"
    email = f"{roll_number.lower()}@sreenidhi.edu.in"
    
    data.append([name, roll_number, email])

csv_filename = "../student_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Roll Number', 'Email Address']) 
    writer.writerows(data)

