import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        """Add stocks to the portfolio"""
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol}.")

    def remove_stock(self, symbol, shares):
        """Remove stocks from the portfolio"""
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed {symbol} from the portfolio.")
            else:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol}.")
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def get_portfolio_value(self):
        """Fetch real-time stock prices and calculate total portfolio value"""
        total_value = 0.0
        for symbol, shares in self.portfolio.items():
            stock = yf.Ticker(symbol)
            price = stock.history(period='1d')['Close'].iloc[-1]
            total_value += price * shares
            print(f"{symbol}: {shares} shares @ ${price:.2f} per share")
        print(f"Total Portfolio Value: ${total_value:.2f}")

# Example Usage
if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("TSLA", 5)
    portfolio.remove_stock("AAPL", 3)
    portfolio.get_portfolio_value()
