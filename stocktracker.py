# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker")

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? "))

# To store portfolio details
portfolio = []

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        portfolio.append([stock_name, quantity, price, investment])

        print("Stock Price:", price)
        print("Investment Value:", investment)

    else:
        print("Stock not found!")

# Display total investment
print("\nTotal Investment Value:", total_investment)

# Save result to a text file
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Details\n")
file.write("-------------------------\n")

for item in portfolio:
    file.write(
        f"Stock: {item[0]}, Quantity: {item[1]}, "
        f"Price: {item[2]}, Investment: {item[3]}\n"
    )

file.write(f"\nTotal Investment Value: {total_investment}")

file.close()

print("\nPortfolio details saved in portfolio.txt")