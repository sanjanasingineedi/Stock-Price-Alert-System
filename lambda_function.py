import json
import requests
import boto3
import os

# Set up SNS client
sns = boto3.client('sns')

# Set up stock API details
STOCK_API_KEY = os.getenv("STOCK_API_KEY", "demo")  # Add your Alpha Vantage API key in Lambda environment variables
STOCK_SYMBOL = os.getenv("STOCK_SYMBOL", "IBM")  # You can change the stock symbol (AAPL for Apple)

# SNS topic ARN (replace with your actual ARN)
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN", "arn:aws:sns:us-east-1:590184086939:StockPriceAlerts")

# Threshold values
UPPER_THRESHOLD = float(os.getenv("UPPER_THRESHOLD", 150.00))  # Upper threshold example
LOWER_THRESHOLD = float(os.getenv("LOWER_THRESHOLD", 100.00))  # Lower threshold example

def get_stock_price(symbol):
    # Alpha Vantage API URL
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_API_KEY}&interval=1min&apikey={STOCK_TOPIC_ARN}"
    response = requests.get(url)
    data = response.json()
    
    # Extract the latest stock price
    time_series = data.get("Time Series (1min)", {})
    if not time_series:
        return None

    latest_time = sorted(time_series.keys())[0]
    latest_price = float(time_series[latest_time]["1. open"])

    return latest_price

def lambda_handler(event, context):
    # Get the current stock price
    stock_price = get_stock_price(STOCK_SYMBOL)
    
    if stock_price is None:
        print("Could not fetch stock price")
        return {"statusCode": 500, "body": json.dumps("Stock price fetch failed")}

    print(f"Current {STOCK_SYMBOL} price: {stock_price}")

    # Check if the stock price exceeds the upper threshold
    if stock_price > UPPER_THRESHOLD:
        message = f"The stock price of {STOCK_SYMBOL} is ${stock_price}, which exceeds your upper threshold of ${UPPER_THRESHOLD}!"
        
        # Send an SNS notification for upper threshold
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=f"{STOCK_SYMBOL} Stock Price Alert: Above Threshold"
        )
        print("Upper threshold alert sent!")
    
    # Check if the stock price falls below the lower threshold
    elif stock_price < LOWER_THRESHOLD:
        message = f"The stock price of {STOCK_SYMBOL} is ${stock_price}, which is below your lower threshold of ${LOWER_THRESHOLD}!"
        
        # Send an SNS notification for lower threshold
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=f"{STOCK_SYMBOL} Stock Price Alert: Below Threshold"
        )
        print("Lower threshold alert sent!")

    else:
        print(f"The stock price of {STOCK_SYMBOL} is within the threshold range.")

    return {"statusCode": 200, "body": json.dumps(f"Checked stock price: ${stock_price}")}
