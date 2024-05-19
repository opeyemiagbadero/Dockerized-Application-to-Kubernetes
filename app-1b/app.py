import os
from flask import Flask

app = Flask(__name__)

# Get the value of the ENV environment variable, default to 'dev' if not set
ENV = os.environ.get('ENV', 'dev')

@app.route('/')
def hello():
    return f'Hello {ENV.capitalize()} Kube'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
