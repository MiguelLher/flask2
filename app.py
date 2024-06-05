from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Te amo Narhaly"


if __name__ == '__main__':
    app.run(debug=True)