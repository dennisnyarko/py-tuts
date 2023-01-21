import csv

name = input("Whats your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])