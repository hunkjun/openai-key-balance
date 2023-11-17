
import requests

from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/subscription', methods=['GET','POST'])
def get_subscription():
    queryUrl = 'https://api.openai.com/dashboard/billing/subscription'
    # get Authorization
    key = request.headers.get('Authorization')
    print(key)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Authorization': key,
        'Accept': '*/*',
        'Host': 'api.openai.com',
        'Connection': 'keep-alive'
    }
    print(headers)
    r = requests.get(queryUrl, headers=headers)
    return r.json()

@app.route('/usage', methods=['GET','POST'])
def get_usage():
    queryUrl = 'https://api.openai.com/v1/dashboard/billing/usage'
    # get Authorization
    key = request.headers.get('Authorization')
    end_date = request.args.get("end_date")
    start_date = request.args.get("start_date")
    print(key)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Authorization': key,
        'Accept': '*/*',
        'Host': 'api.openai.com',
        'Connection': 'keep-alive'
    }
    print(headers)
    data = {
        "start_date":  start_date,
        "end_date": end_date
    }
    print(data)
    r = requests.get(queryUrl, headers=headers, params=data)
    return r.json()

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    # print("key:", get_usage())
    app.run()

