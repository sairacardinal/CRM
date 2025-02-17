class SalesTracking:
    def __init__(self):
        self.sales = []

    def record_sale(self, customer_name, product, amount):
        sale = {"Customer": customer_name, "Product": product, "Amount": amount}
        self.sales.append(sale)
        return f"Sale recorded for {customer_name}: {product} - ${amount}"

    def get_sales(self):
        return self.sales