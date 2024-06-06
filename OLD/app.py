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
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #fff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                text-align: center;
            }
            img {
                max-width: 100%;
                height: auto;
                border-radius: 10px;
                margin-bottom: 20px;
            }
            h1 {
                color: #333;
                margin-bottom: 10px;
            }
            h2 {
                color: #666;
                margin-bottom: 20px;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
                color: #444;
            }
            .footer {
                margin-top: 20px;
                font-size: 14px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*cG6U1qstYDijh9bPL42e-Q.jpeg" alt="Miguel Lara Hernandez">
            <h1>Miguel Lara Hernandez</h1>
            <h2>9 A - 20200705</h2>
            <p>Bienvenido a mi página de presentación personal. Aquí encontrarás información sobre mí y mis proyectos.</p>
            <div class="footer">© 2024 Miguel Lara Hernandez</div>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)
