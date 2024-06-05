from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Miguel Lara Hernandez - 9 A - 20200705"


if __name__ == '__main__':
    app.run(debug=True)