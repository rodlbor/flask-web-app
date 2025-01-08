from urllib.parse import quote as url_quote
from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def fetch_latest_news():
    api_key = os.getenv('NEWS_API_KEY')  # Get API key from environment variable
    if not api_key:
        raise ValueError("NEWS_API_KEY environment variable not set")
    
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch news. Status code: {response.status_code}")
    
    data = response.json()
    return data.get('articles', [])[:5]  # Get top 5 articles or an empty list if missing

@app.route('/')
def home():
    try:
        news = fetch_latest_news()
    except Exception as e:
        return f"<h1>Error:</h1><p>{e}</p>", 500  # Display the error in the browser
    return render_template("index.html", news=news)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

