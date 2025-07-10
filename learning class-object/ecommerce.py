class EcommerceVendor():
    def __init__(self,name):
        self.name = name

    def register(self,date_of_birth,product):
        self.date_of_birth = date_of_birth
        self.total_products = product
        print(f"{self.name} is successfully registered")

    def add_product(self,new_product):
        self.total_products += new_product
        print(f"added successfully. total proudct is {self.total_products}")


a1 = EcommerceVendor("Aakash")
a1.register(87876868,1)
# class VendroDashboard(EcommerceVendor):
#     def add_product(product):
#         total_proudcts += product
#         print(f"added successfully. total proudct is {total_proudcts}")

a1.add_product(343)
