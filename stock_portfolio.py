import requests

# Initialize an empty portfolio
portfolio = {}

# Replace with your Alpha Vantage API key
API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

def fetch_stock_price(ticker):
    """Fetch real-time stock price from Alpha Vantage API."""
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": ticker,
        "apikey": API_KEY
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        else:
            print(f"Could not fetch data for {ticker}.")
            return None
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        return None

def add_stock(ticker, shares):
    """Add a stock to the portfolio."""
    ticker = ticker.upper()
    if ticker in portfolio:
        portfolio[ticker] += shares
    else:
        portfolio[ticker] = shares
    print(f"Added {shares} shares of {ticker} to your portfolio.")

def remove_stock(ticker, shares):
    """Remove a stock from the portfolio."""
    ticker = ticker.upper()
    if ticker in portfolio:
        if portfolio[ticker] > shares:
            portfolio[ticker] -= shares
            print(f"Removed {shares} shares of {ticker} from your portfolio.")
        elif portfolio[ticker] == shares:
            del portfolio[ticker]
            print(f"Removed all shares of {ticker}.")
        else:
            print(f"You don't own enough shares of {ticker} to remove.")
    else:
        print(f"{ticker} is not in your portfolio.")

def view_portfolio():
    """Display the portfolio with real-time stock prices."""
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\nYour Portfolio:")
    total_value = 0
    for ticker, shares in portfolio.items():
        price = fetch_stock_price(ticker)
        if price:
            total = shares * price
            total_value += total
            print(f"{ticker}: {shares} shares @ ${price:.2f} = ${total:.2f}")
        else:
            print(f"Could not retrieve price for {ticker}.")
    print(f"Total Portfolio Value: ${total_value:.2f}")

# Main Program
if __name__ == "__main__":
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter stock ticker (e.g., AAPL): ")
            shares = int(input("Enter the number of shares: "))
            add_stock(ticker, shares)
        elif choice == "2":
            ticker = input("Enter stock ticker (e.g., AAPL): ")
            shares = int(input("Enter the number of shares to remove: "))
            remove_stock(ticker, shares)
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")