stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stocks.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stocks:
        print("Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    price = stocks[stock_name]
    investment = price * quantity

    portfolio.append((stock_name, quantity, price, investment))
    total_investment += investment

    print(f"{stock_name} added successfully.")
    print(f"Investment value: ${investment}")

print("\n" + "=" * 45)
print("          PORTFOLIO SUMMARY")
print("=" * 45)

if portfolio:
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Value':<10}")
    print("-" * 40)

    for stock, quantity, price, value in portfolio:
        print(f"{stock:<10}{quantity:<10}${price:<9}${value:<10}")

    print("-" * 40)
    print(f"Total Investment: ${total_investment}")
else:
    print("No stocks were added.")

print("=" * 45)
