from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def fetch_latest_news():
    api_key = '46b2085e855839b26e5de5f3d7d4a713'  # Your API key
    url = f"http://api.mediastack.com/v1/news?access_key={api_key}&countries=ar&limit=5&sort=published_desc"
    response = requests.get(url)
    data = response.json()
    return data['data']  # Adjusted based on mediastack's response structure

@app.route('/')
def home():
    news = fetch_latest_news()
    return render_template("index.html", news=news)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

