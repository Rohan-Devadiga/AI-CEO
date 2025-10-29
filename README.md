# AI CEO - Jeff Bezos Replica

AI CEO is an AI-powered chatbot that simulates Jeff Bezos.  
If Jeff Bezos is unavailable, you can interact with his AI version.  
Additionally, the AI can provide **live Amazon stock prices** using the `yfinance` library.

---

## Project Overview

AI CEO is designed to give users an interactive experience with a virtual version of Jeff Bezos.  
It can answer business questions, provide insights, and even fetch live Amazon stock prices.  

---

## Tech Stack

- **Python** – main programming language  
- **GEMINI API** – for chat responses  
- **yfinance** – for real-time stock data  
- **.env** – to safely store API keys  
- **VS Code / Terminal** – recommended environment  

---

## How It Works

1. User sends a message to the AI CEO.  
2. The AI generates a response using a language model.  
3. If the user asks for Amazon’s stock price, the AI fetches live data using `yfinance`.  
4. The conversation continues interactively.  

---

## Use Cases

- Ask for business advice from Jeff Bezos’ AI.  
- Get Amazon’s live stock price quickly.  
- Fun interaction for tech enthusiasts and investors.  
## Installation

1. **Clone the repository:**
2. 
git clone https://github.com/Rohan-Devadiga/AI-CEO.git
cd AI-CEO

### 2. Create a Virtual Environment (Recommended)
python -m venv venv

### 3. Activate the Virtual Environment
On Windows:<br>
venv\Scripts\activate

On macOS/Linux:<br>
source venv/bin/activate

### 4. Install Dependencies
pip install -r requirements.txt

### 5. Add Your API Key<br>
Before running the project, you must add your own API key.<br>
Create a file named .env in the root directory and add the following line:<br>
KEY="GEMINI_API_KEY"<br>

### 6. Run the Main
python main.py
