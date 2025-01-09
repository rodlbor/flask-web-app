from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Fetch latest news from Argentina in Spanish
def fetch_latest_news():
    api_key = os.getenv('NEWS_API_KEY')  # Get the API key from the environment
    url = f"https://newsapi.org/v2/top-headlines?country=ar&language=es&apiKey={api_key}"  # Argentina news in Spanish
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('articles', [])  # Return the articles if available
    else:
        return []

@app.route('/')
def home():
    news = fetch_latest_news()
    return render_template("index.html", news=news)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

