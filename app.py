from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Miguel Lara Hernandez</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f4f4f9;
                color: #333;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            img {
                max-width: 100%;
                height: auto;
                border-radius: 8px;
            }
            h1, h2 {
                color: #333;
            }
            p {
                font-size: 16px;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Miguel Lara Hernandez</h1>
            <h2>9 A - 20200705</h2>
            <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*cG6U1qstYDijh9bPL42e-Q.jpeg" alt="Miguel Lara Hernandez">
            <p>Bienvendio a mi página de presentación personal. Aquí encontrarás información sobre mí y mis proyectos.</p>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)
