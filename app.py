from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')
    return f"Nombre: {name}, Mensaje: {message}"

if __name__ == '__main__':
    app.run(debug=True)
