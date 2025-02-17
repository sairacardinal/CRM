from CustomerManagement import CustomerManagement
from SalesTracking import SalesTracking
from Reporting import Reporting
from faker import Faker
import random

if __name__ == "__main__":
    customer_mgmt = CustomerManagement()
    sales_mgmt = SalesTracking()
    report_mgmt = Reporting(customer_mgmt, sales_mgmt)
    fake = Faker()

    # Predefined list of realistic product names
    product_list = [
        "Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch",
        "Gaming Console", "Wireless Earbuds", "Monitor", "Keyboard", "Mouse"
    ]

    # Generate 10 customers and store their details
    customers = []  # Separate list to store only names
    for _ in range(10):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        print(customer_mgmt.add_customer(name, email, phone))
        customers.append(name)  # Store names separately for easier access

    # Generate and record sales for each customer using actual names
    for name in customers:
        product = fake.random_element(product_list)  # Select a random product
        price = round(random.uniform(50, 2000), 2)  # Generate a realistic price
        print(sales_mgmt.record_sale(name, product, price))  # Correctly prints actual name

    # Generating Report
    print(report_mgmt.generate_report())
