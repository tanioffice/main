#!/usr/bin/env python3

import csv
from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    name: str
    hours_worked: float
    hourly_rate: float

    def calculate_pay(self) -> float:
        return self.hours_worked * self.hourly_rate

def read_employees(csv_path: str) -> List[Employee]:
    employees = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employees.append(
                Employee(
                    name=row['name'],
                    hours_worked=float(row['hours_worked']),
                    hourly_rate=float(row['hourly_rate'])
                )
            )
    return employees

def main(csv_path: str):
    employees = read_employees(csv_path)
    total_payroll = 0.0
    for emp in employees:
        pay = emp.calculate_pay()
        total_payroll += pay
        print(f"{emp.name}: {pay:.2f}")
    print(f"Total Payroll: {total_payroll:.2f}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple payroll calculator")
    parser.add_argument('csv', help='Path to employee CSV file')
    args = parser.parse_args()

    main(args.csv)

