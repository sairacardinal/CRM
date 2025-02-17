class CustomerManagement:
    def __init__(self):
        self.customers = []

    def add_customer(self, name, email, phone):
        customer = {"Name": name, "Email": email, "Phone": phone}
        self.customers.append(customer)
        return f"Customer {name} added successfully."

    def get_customers(self):
        return self.customers