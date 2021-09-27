from quantel import Quantel

# Authenticate with the API
qt = Quantel(api_key="PLACEHOLDER")

# Instantiate the ticker class
goog = qt.ticker('goog', asynchronous=True)

# Retrieve company profile
data = goog.profile()

print(data)
