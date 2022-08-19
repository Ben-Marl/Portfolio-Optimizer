import PortfolioOptimizer as PortOpt

# Function to calculate portfolio 
def Calculate_portfolio(tickers):
	maxlist, minlist, max_return, min_risk = PortOpt.optimize(tickers)
	return  maxlist, minlist, max_return, min_risk