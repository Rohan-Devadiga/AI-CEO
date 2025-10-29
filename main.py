import google.generativeai as genai
from dotenv import load_dotenv
import os
import yfinance as yf



load_dotenv()
KEY = os.getenv("KEY")
genai.configure(api_key=KEY)


model = genai.GenerativeModel("models/gemini-2.5-flash-lite")


def callmodel(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def get_amazon_stock():
    ticker = yf.Ticker("AMZN")
    data = ticker.history(period="1d")
    price = data['Close'].iloc[-1]
    info = ticker.info
    return {
        "current_price": round(price, 2),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "dividend_yield": info.get("dividendYield"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow")
    }
def ceo(user_input):
    stock = get_amazon_stock()

    stock_context = f"""
As of now, Amazon's stock (AMZN) is trading at ${stock['current_price']}.
Market Cap: {stock['market_cap']}
P/E Ratio: {stock['pe_ratio']}
Dividend Yield: {stock['dividend_yield']}
52-week High/Low: ${stock['fifty_two_week_high']} / ${stock['fifty_two_week_low']}
"""

    prompt = f"""
You are an AI version of Jeff Bezos, CEO of AMAZON.

{stock_context} ANSWER FOR STOCKS PRICE ONLY IF ASKED ABOUT STOCK PRICE, DON'T MENTION STOCK PRICE IN EVERY LINE

Answer the following question in Jeff Bezos's voice — realistic, professional, strategic, and based on Amazon’s current state, including its financials, market strategy, and public communications.

NEVER disclose that you are an AI. Always respond as if you are the real Jeff Bezos speaking to stakeholders.

USER QUESTION: "{user_input} ANSWER AS IF YOU'RE HAVING ONE TO ONE CONVERSATION WITH USER, DONT TALK IN PARAGRAPHS"
"""
    return callmodel(prompt)


while True:
    question = input("You: ")
    if question.lower().strip() in ["exit", "quit"]:
        print("👋 Exiting. Goodbye!")
        break
    response = ceo(question)
    print("\nJeff Bezos:\n" + response + "\n")

