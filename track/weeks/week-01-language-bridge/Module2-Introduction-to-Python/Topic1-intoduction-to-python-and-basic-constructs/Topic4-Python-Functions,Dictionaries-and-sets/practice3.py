def display_invoice_total(price,quantity):
    total=price*quantity
    print("Total:",total)

price=int(input("enter price:"))
quantity=int(input("enter quantity:"))

display_invoice_total(price,quantity)