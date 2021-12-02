"""
Name: Lydia Heath
sales_force.py

Purpose: Creating a class for the sales force.

Certificate of Authenticity:
I certify this work is entirely my own with help from Hunter Ross.
"""

from sales_person import SalesPerson


class SalesForce:
    """
    Class that puts together and compares the sales force.
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file):
        in_file = open(file, 'r')
        lines = in_file.readlines()
        for line in lines:
            line = line.split(", ")
            person = SalesPerson(line[0], line[1])
            sales = line[2].split()
            for sale in sales:
                person.enter_sale(float(sale))
            self.sales_people.append(person)

    def quota_report(self, quota):
        report_list = []
        for person in self.sales_people:
            report_list.append([person.get_id(), person.get_name(),
                                person.total_sales(), person.met_quota(quota)])
        return report_list

    def top_seller(self):
        top = []
        for i in range(len(self.sales_people)):
            highest = self.sales_people[i]
            for j in range(i + 1, len(self.sales_people)):
                if self.sales_people[j].get_sales() > highest.get_sales():
                    highest = self.sales_people[j]
        top.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i].total_sales() == top[0].total_sales():
                top.append(self.sales_people[i])
        return top

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
