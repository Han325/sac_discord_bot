import requests

# URL of the webpage you want to download
url = "https://finance.yahoo.com/quote/%5EGSPC/?guccounter=1"

# Send HTTP request to the specified URL and save the response from server in a response object called r
r = requests.get(url)

# Print the webpage content to the console
print(r.text)
