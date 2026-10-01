# PYTHON PRACTICAL PROGRAMMING ASSIGNMENT.
# MAMA MBOGA DIGITAL STALL POS

def prompt_Quantity(item_name):
    while True:
        try:
            unit = "kg" if item_name in ["tomatoes","onions"] else "bunches"
            Quantity = float(input("Enter quantity (kg/bunches):"))
            if Quantity <= 0.0:
                print("Error: Quantity must exceed 0.0 kg")
                continue
            return Quantity
        except ValueError:
            print("Error: Please enter a numeric value")

def calculate_item_price(item_name, Quantity, Customer_type="retail"):
    retail_price = {"tomatoes": 3000, "onions": 2500, "matooke": 25000}
    wholesale_price = {"tomatoes": 2400, "onions": 2000, "matooke": 20000}
    
    if Customer_type == "wholesale":
        if item_name == "matooke" and Quantity < 3:
            unit_price = retail_price[item_name]
        else:
            unit_price = wholesale_price[item_name]
        total = Quantity * unit_price
        return total, unit_price
    else:
        unit_price = retail_price[item_name]
        if item_name in ["tomatoes","onions"] and Quantity > 5:
            normal_price = 5 * unit_price
            discount_price = unit_price * 0.95
            extra_part = (Quantity - 5) * discount_price
            total = normal_price + extra_part
        else:
            total = Quantity * unit_price
        return total, unit_price

def apply_market_levy_and_packaging(subtotal, needs_eco_crate=False):
    market_levy = subtotal * 0.02  # 2% market levy
    crate_cost = 5000 if needs_eco_crate else 0
    grand_total = subtotal + market_levy + crate_cost
    return grand_total, market_levy, crate_cost

# --- MAIN PROGRAM ---
print("MAMA MBOGA DIGITAL STALL POS".center(58))
print("="*58)
Customer_name = input("\nCustomer's Name: ")
Customer_type = input("Customer Type (retail/wholesale): ")
while Customer_type not in ["retail","wholesale"]:
    print("Error: Type retail or wholesale.")
    Customer_type = input("Customer Type (retail/wholesale): ")

basket = []
subtotal = 0

while True:
    item_name = input("\nAdd Item (tomatoes / onions / matooke / done): ")
    if item_name == "done":
        break
    if item_name not in ["tomatoes", "onions", "matooke"]:
        print("Error: Invalid Item")
        continue
    Quantity = prompt_Quantity(item_name)
    unit = "kg" if item_name in ["tomatoes","onions"] else "bunches"
    item_total, unit_price = calculate_item_price(item_name, Quantity, Customer_type)
    print(f"Added {Quantity} {unit} of {item_name} @ {unit_price} = {item_total}")
    basket.append({"item": item_name, "qty": Quantity, "unit_price": unit_price, "total": item_total})
    subtotal += item_total

crate_input = input("Add reusable Delivery crate? (Yes/No): ")
needs_crate = True if crate_input == "Yes" else False

grand_total, levy, crate_cost = apply_market_levy_and_packaging(subtotal, needs_crate)

# Receipt
print()
print("-"*58)
print("RECEIPT #STALL-042".center(58))
print(f"Customer: {Customer_name} ({Customer_type})")
print("-"*58)
print(f"{'Item':<12} {'Qty':<8} {'Unit':<12} {'Subtotal':<12}")
print("-"*58)
for entry in basket:
    print(f"{entry['item']:<12} {entry['qty']:<8} {entry['unit_price']:<12} {entry['total']:<12}")
print("-"*58)
print(f"{'Subtotal:':<30} {subtotal}")
print(f"{'Market Levy (2%):':<30} {levy}")
print(f"{'Crate Cost:':<30} {crate_cost}")
print("-"*58)
print(f"{'GRAND TOTAL:':<30} {grand_total}")
print("-"*58)