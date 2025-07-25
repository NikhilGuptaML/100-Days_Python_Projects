# 📈 Stock Price Alert with News & SMS Notification

This project tracks a selected stock (e.g., RELIANCE.BSE) and sends you an SMS alert via Twilio if the stock price changes significantly (more than 2%) in a day. It also fetches and includes top news headlines related to the company to help explain the movement.

---

## 🚀 Features

- 📉 Real-time stock monitoring using Alpha Vantage API  
- 📰 News headline fetching via NewsAPI  
- 📲 SMS alert using Twilio when price change crosses a threshold  
- 🔐 Secrets managed securely via `.env` file  
- ⚙️ Fully modular and easy to adapt to other stocks

---

## 📦 Tech Stack

- Python 3  
- [Alpha Vantage API](https://www.alphavantage.co/)  
- [NewsAPI](https://newsapi.org/)  
- [Twilio](https://www.twilio.com/) for SMS alerts  
- `requests`, `python-dotenv`, `twilio`

---

## 📂 Project Structure

Project_3_Stock_Alert/
│
├── main.py # Core logic
├── .env.example 
└── README.md # Project documentation

---

## 🔧 Environment Variables

Create a `.env` file based on the `.env.example` template and add your API credentials:

```env
API_KEY_STOCK=your_alpha_vantage_api_key
API_KEY_NEWS=your_newsapi_key
AUTH_TOKEN=your_twilio_auth_token
account_sid=your_twilio_sid
INCOMING_NO=your_twilio_number
OUTGOING_NO=your_verified_number
Messaging_Service_SID=your_msg_service_sid

🛠️ How to Run
1. Install dependencies:
    pip install -r requirements.txt
2. Add your credentials in .env file
3. Run the script:
    python main.py
You’ll receive an SMS if the stock price moves beyond the threshold with two top news articles.

📈 Default Settings
Stock Tracked: RELIANCE.BSE

Change Threshold: ±2%

News Quantity: 2 articles

News Sort: Popularity

You can modify STOCK, COMPANY_NAME, and the threshold inside main.py as needed.

🔐 Security
.env is excluded from GitHub using .gitignore to prevent leaking sensitive data.

Only .env.example is shared for reference.


📬 Contact
Feel free to reach out or connect if you have questions or feedback!