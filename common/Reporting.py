class Reporting:
    def __init__(self, customer_mgmt, sales_mgmt):
        self.customer_mgmt = customer_mgmt
        self.sales_mgmt = sales_mgmt

    def generate_report(self):
        report = {
            "Total Customers": len(self.customer_mgmt.get_customers()),
            "Total Sales": len(self.sales_mgmt.get_sales()),
            "Revenue": sum(sale["Amount"] for sale in self.sales_mgmt.get_sales()),
        }
        return report