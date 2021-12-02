"""
Name: Lydia Heath
sales_person.py

Purpose: Class for sales person.

Certificate of Authenticity:
I certify this work is entirely my own with help from Hunter Ross.
"""


class SalesPerson:
    """
    Class to create a sales person on a sales force.
    """
    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for i in range(0, len(self.sales)):
            total = total + self.sales[i]
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        return bool(self.total_sales() >= quota)

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        if other.total_sales() == self.total_sales():
            return 0

    def __str__(self):
        return str(self.employee_id) + "-" + self.name + ":" + str(self.total_sales())
    