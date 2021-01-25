import requests
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
"""
Dotenv lifecycle:
1. import module: from dotenv import ...
2. load_dotenv()
3. The key/value pairs from the .env file is now present as system environmental variables
    and can be accessed via:
4. os.getenv()
"""

load_dotenv()
SECRET_KEY = os.getenv("EMAIL")

app = Flask(__name__)

"""
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            url = request.form['url']
            r = requests.get(url)
            print(r.text)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('index.html', errors=errors, results=results)


if __name__ == '__main__':
    print(SECRET_KEY)
    app.run(host='0.0.0.0')