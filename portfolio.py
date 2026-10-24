
import csv
from datetime import datetime

# Sample stock prices for practice only (not live market prices)
stock_prices = {
    "AAPL": 230.00,
    "MSFT": 500.00,
    "GOOGL": 250.00,
    "AMZN": 220.00,
    "NVDA": 180.00
}

portfolio = []

print("=" * 50)
print("       INVESTMENT PORTFOLIO TRACKER")
print("=" * 50)
print("Available sample tickers:", ", ".join(stock_prices))

while True:
    ticker = input("\nEnter stock ticker (or DONE to finish): ").strip().upper()

    if ticker == "DONE":
        break

    if ticker not in stock_prices:
        print("Ticker not available. Please choose a listed ticker.")
        continue

    try:
        buy_price = float(input("Enter your buy price per share: "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Buy price and quantity must be positive.")
            continue

    except ValueError:
        print("Please enter a valid price and whole-number quantity.")
        continue

    current_price = stock_prices[ticker]
    invested = buy_price * quantity
    market_value = current_price * quantity
    gain_loss = market_value - invested
    percentage = (gain_loss / invested) * 100

    portfolio.append({
        "Ticker": ticker,
        "Buy Price": buy_price,
        "Quantity": quantity,
        "Sample Current Price": current_price,
        "Invested Amount": invested,
        "Market Value": market_value,
        "Gain/Loss": gain_loss,
        "Gain/Loss %": percentage
    })

if not portfolio:
    print("\nNo holdings entered. No CSV report created.")
else:
    total_invested = sum(item["Invested Amount"] for item in portfolio)
    total_value = sum(item["Market Value"] for item in portfolio)
    total_gain_loss = total_value - total_invested
    total_percentage = (total_gain_loss / total_invested) * 100

    print("\n" + "=" * 75)
    print("PORTFOLIO SUMMARY")
    print("=" * 75)

    for item in portfolio:
        print(
            f"{item['Ticker']}: "
            f"Invested = ${item['Invested Amount']:.2f}, "
            f"Value = ${item['Market Value']:.2f}, "
            f"Gain/Loss = ${item['Gain/Loss']:.2f} "
            f"({item['Gain/Loss %']:.2f}%)"
        )

    print("-" * 75)
    print(f"Total Invested: ${total_invested:.2f}")
    print(f"Total Market Value: ${total_value:.2f}")
    print(f"Total Gain/Loss: ${total_gain_loss:.2f}")
    print(f"Total Gain/Loss %: {total_percentage:.2f}%")

    # Save the report to a CSV file
    filename = "portfolio_summary.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "Ticker", "Buy Price", "Quantity",
            "Sample Current Price", "Invested Amount",
            "Market Value", "Gain/Loss", "Gain/Loss %"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in portfolio:
            formatted_item = {
                key: (
                    round(value, 2) if isinstance(value, float) else value
                )
                for key, value in item.items()
            }
            writer.writerow(formatted_item)

        writer.writerow({})
        writer.writerow({
            "Ticker": "TOTAL",
            "Invested Amount": round(total_invested, 2),
            "Market Value": round(total_value, 2),
            "Gain/Loss": round(total_gain_loss, 2),
            "Gain/Loss %": round(total_percentage, 2)
        })

    print(f"\nReport saved successfully to {filename}")
    print("Note: Sample prices are for practice, not live market data.")
