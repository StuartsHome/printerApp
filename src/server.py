
from flask import Flask
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

server = Flask(__name__)


@server.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    print(SECRET_KEY)
    server.run(host='0.0.0.0')