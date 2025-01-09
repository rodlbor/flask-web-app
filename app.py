# rodbor 1123

from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def fetch_latest_news():
    api_key = os.getenv('NEWS_API_KEY')  # Get API key from environment variable
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=8a11b1002cf6437299befc225e850158"
    response = requests.get(url)
    data = response.json()
    return data['articles'][:5]  # Get top 5 articles

@app.route('/')
def home():
    news = fetch_latest_news()
    return render_template("index.html", news=news)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

