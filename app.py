from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import logging

app = Flask(__name__)

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)

# Cargar el modelo entrenado
model = joblib.load('modeloo.pkl')
app.logger.debug('Modelo cargado correctamente.')

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos enviados en el request
        app.logger.debug(f'Datos recibidos: {request.form}')
        na_sales = float(request.form['na_sales'])
        eu_sales = float(request.form['eu_sales'])
        jp_sales = float(request.form['jp_sales'])
        other_sales = float(request.form['other_sales'])
        genre = float(request.form['genre'])
        platform = float(request.form['platform'])

        # Crear un DataFrame con los datos
        data_df = pd.DataFrame([[na_sales, eu_sales, jp_sales, other_sales, genre, platform]], 
                               columns=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Genre', 'Platform'])
        app.logger.debug(f'DataFrame creado: {data_df}')

        # Realizar predicciones
        prediction = model.predict(data_df)
        app.logger.debug(f'Predicción: {prediction[0]}')

        # Devolver las predicciones como respuesta JSON
        return jsonify({'global_sales': prediction[0]})
    except Exception as e:
        app.logger.error(f'Error en la predicción: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
