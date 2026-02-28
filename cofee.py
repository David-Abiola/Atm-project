from datetime import datetime

class Coffee:
    def __init__(self, vanilla= 2, choco= 2, berry= 2):
        self.stock = {
            "vanilla": vanilla,
            "choco": choco,
            "berry": berry
        }
        self.price = 250

    def payment(self):
        order = input("Enter product to order (vanilla/choco/berry): ").lower()
        if order == "1":
            print()
        if order not in self.stock:
            print("Product not available.")
            return
        while order in self.stock:
            try:
                quantity = int(input("Enter quantity: "))
                if self.stock[order] < quantity:
                    print(f"we don't have up to that in our store")
                    break

                paid_amount = int(input("Enter amount to pay: "))
                total_cost = self.price * quantity

                if paid_amount >= total_cost:
                    print(f"you've successfully purchased {order} at {datetime.now()}")
                    self.stock[order] -= quantity
                    if paid_amount > total_cost:
                        print(f"Change returned: {paid_amount - total_cost}")
                    rerun = int(input("enter 1 to run the program again and 2 to quit "))
                    if rerun == 1:
                        coffee.payment()
                    if rerun == 2:
                        break
                    else:
                        raise ValueError("wrong value inputted")
                else:
                    print(f"Incorrect amount. You need {total_cost}.")

            except ValueError:
                print("Please enter numeric values for quantity and payment.")


print("Welcome to david's coffee machine")
print(f"""
Available products:
Vanilla    = 250
Chocolate  = 250
Strawberry = 250
""")
coffee = Coffee()
product = Coffee(2,2,2)
try:
    enter = int(input("Enter 1 to order and 2 to check numbers of product in our stock and 3 to exit and: "))
    if enter == 1:
        coffee.payment()
    if enter == 2:
        print(product.stock)
    else:
        print()
except ValueError:
    print("Wrong value inputted.")

