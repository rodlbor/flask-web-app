from flask import Flask, jsonify
import requests

app = Flask(__name__)

def fetch_latest_news():
    api_key = '8a11b1002cf6437299befc225e850158'  # Hardcoded API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Failed to fetch news: {response.status_code}")

@app.route('/news', methods=['GET'])
def get_news():
    try:
        news_data = fetch_latest_news()
        return jsonify(news_data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

